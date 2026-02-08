#!/usr/bin/env python3
"""
Lumerical文档质量优化脚本

功能：
1. 更新文档链接：相对路径链接 → 完整URL或本地相对链接
2. 统一格式化：使用mdformat对所有Markdown文档进行格式化
3. 索引转换：将命令列表转换为三列表格格式
4. 链接验证：检查所有外部链接的有效性（异步HTTP HEAD）

支持：
- 断点续传：记录处理状态，支持中断后恢复
- 分批处理：每批处理指定数量的文件
- 验证报告：生成详细的优化结果报告
"""

import asyncio
import json
import re
import time

# 可选依赖
try:
    import aiohttp

    HAS_AIOHTTP = True
except ImportError:
    aiohttp = None
    HAS_AIOHTTP = False
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set, Any, Union
from dataclasses import dataclass, asdict
from enum import Enum
import hashlib
import subprocess
import sys


# ============================================================================
# 配置常量
# ============================================================================


class Config:
    """全局配置"""

    # 路径配置
    BASE_DIR = Path(__file__).parent.parent
    DOCS_EN_DIR = BASE_DIR / "docs" / "lsf-script" / "en"
    INDEX_FILE = (
        BASE_DIR / "docs" / "lsf-script" / "lsf-script-commands-alphabetical.md"
    )

    # 备份配置
    BACKUP_DIR = BASE_DIR / "backup" / "en_backup_20260208"

    # 处理配置
    BATCH_SIZE = 50  # 每批处理的文件数
    MAX_CONCURRENT_REQUESTS = 10  # 最大并发HTTP请求数

    # 链接检查配置
    REQUEST_TIMEOUT = 10  # HTTP请求超时时间（秒）
    MAX_RETRIES = 3  # 最大重试次数

    # 检查点配置
    CHECKPOINT_FILE = BASE_DIR / "optimization_checkpoint.json"
    PROGRESS_FILE = BASE_DIR / "optimization_progress.json"
    ERROR_LOG = BASE_DIR / "optimization_errors.json"

    # 报告配置
    REPORT_FILE = BASE_DIR / "optimization_report.json"

    # 链接模式
    BASE_URL = "https://optics.ansys.com"
    LIST_OF_COMMANDS_URL = f"{BASE_URL}/hc/en-us/articles/360037228834"

    # 文件名编码映射（从update_lsf_docs_resume.py复制并修正）
    MULTI_CHAR_REPLACEMENTS = {
        "<=": "lte",
        ">=": "gte",
        "==": "equalsequals",
        "!=": "exclamationequals",
        "+=": "plusequals",
        "-=": "minusequals",
        "*=": "asteriskequals",
        "/=": "slashequals",
    }

    SINGLE_CHAR_REPLACEMENTS = {
        "!": "exclamation",
        '"': "quote",
        "#": "hash",
        "$": "dollar",
        "%": "percent",
        "&": "ampersand",
        "'": "apostrophe",
        "(": "lparen",
        ")": "rparen",
        "*": "asterisk",
        "+": "plus",
        ",": "comma",
        "-": "minus",
        ".": "dot",
        "/": "slash",
        ":": "colon",
        ";": "semicolon",
        "<": "lt",
        "=": "equals",
        ">": "gt",
        "?": "question",
        "@": "at",
        "[": "lbracket",
        "\\": "backslash",
        "]": "rbracket",
        "^": "caret",
        "`": "backtick",
        "{": "lbrace",
        "|": "pipe",
        "}": "rbrace",
        "~": "tilde",
        " ": "_",
    }

    # 反向映射（用于文件名到命令名的转换）
    REVERSE_REPLACEMENTS = {
        v: k for k, v in {**MULTI_CHAR_REPLACEMENTS, **SINGLE_CHAR_REPLACEMENTS}.items()
    }

    # 特殊映射
    SPECIAL_CASES = {
        "dot_cmd": "dot",  # dot_cmd.md → dot 命令
        "dot": ".",  # dot.md → . 命令
        "lbracketrbracket": "[]",  # lbracketrbracket.md → [] 命令
    }


# ============================================================================
# 数据模型
# ============================================================================


class LinkType(Enum):
    """链接类型"""

    COMMAND = "command"  # 命令文档链接
    LIST_OF_COMMANDS = "list_of_commands"  # 命令列表链接
    ARTICLE = "article"  # 非命令文章链接
    EXTERNAL = "external"  # 外部链接
    LOCAL = "local"  # 本地文件链接
    ANCHOR = "anchor"  # 锚点链接


@dataclass
class CommandInfo:
    """命令信息"""

    name: str  # 命令名（如 "addmaterial"）
    filename: str  # 文件名（如 "addmaterial.md"）
    official_url: str  # 官方文档URL
    local_path: str  # 本地文件路径（相对路径）

    def to_dict(self) -> Dict[str, str]:
        return asdict(self)


@dataclass
class LinkInfo:
    """链接信息"""

    url: str  # 原始URL
    link_type: LinkType  # 链接类型
    converted_url: str  # 转换后的URL
    line_number: int  # 行号
    context: str  # 上下文（行内容）

    def to_dict(self) -> Dict[str, Any]:
        return {
            "url": self.url,
            "type": self.link_type.value,
            "converted_url": self.converted_url,
            "line_number": self.line_number,
            "context": self.context[:100],  # 截断
        }


@dataclass
class ValidationResult:
    """验证结果"""

    url: str
    status_code: Optional[int]
    error: Optional[str]
    is_valid: bool
    response_time: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FileProcessingResult:
    """文件处理结果"""

    filename: str
    command_name: str
    links_found: int
    links_converted: int
    formatting_success: bool
    error: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "filename": self.filename,
            "command_name": self.command_name,
            "links_found": self.links_found,
            "links_converted": self.links_converted,
            "formatting_success": self.formatting_success,
            "error": self.error,
        }


# ============================================================================
# 文件名编码/解码工具
# ============================================================================


class FilenameEncoder:
    """文件名编码/解码工具"""

    @staticmethod
    def command_to_filename(command: str) -> str:
        """将命令名转换为文件名"""
        # 检查特殊映射
        if command in Config.SPECIAL_CASES.values():
            for filename, cmd in Config.SPECIAL_CASES.items():
                if cmd == command:
                    return filename

        result = command

        # 先处理多字符组合
        for combo, replacement in Config.MULTI_CHAR_REPLACEMENTS.items():
            result = result.replace(combo, replacement)

        # 处理单字符
        for char, replacement in Config.SINGLE_CHAR_REPLACEMENTS.items():
            result = result.replace(char, replacement)

        # 处理Windows非法字符（可能已被替换）
        illegal_chars = r'<>:"/\\|?*'
        for char in illegal_chars:
            result = result.replace(char, "_")

        # 如果以点开头，添加前缀
        if result.startswith("."):
            result = "dot" + result

        # 如果为空，使用哈希
        if not result:
            result = hashlib.md5(command.encode()).hexdigest()[:8]

        return result

    @staticmethod
    def filename_to_command(filename: str) -> str:
        """将文件名转换回命令名"""
        # 移除.md扩展名
        if filename.endswith(".md"):
            filename = filename[:-3]

        # 检查特殊映射
        if filename in Config.SPECIAL_CASES:
            return Config.SPECIAL_CASES[filename]

        result = filename

        # 反向替换（注意顺序与正向相反）
        # 先替换长的，避免短的重叠
        for replacement, original in Config.REVERSE_REPLACEMENTS.items():
            result = result.replace(replacement, original)

        return result

    @staticmethod
    def get_all_filenames() -> List[str]:
        """获取所有现有的文件名"""
        return [f.name for f in Config.DOCS_EN_DIR.glob("*.md") if f.is_file()]

    @staticmethod
    def find_command_file(command: str) -> Optional[Path]:
        """查找命令对应的文件"""
        filename = FilenameEncoder.command_to_filename(command) + ".md"
        filepath = Config.DOCS_EN_DIR / filename
        return filepath if filepath.exists() else None


# ============================================================================
# 命令映射构建器
# ============================================================================


class CommandMapper:
    """构建命令名、文件名和URL之间的映射关系"""

    def __init__(self):
        self.commands: Dict[str, CommandInfo] = {}
        self.filename_to_command: Dict[str, str] = {}

    def build_from_index(self) -> bool:
        """从索引文件构建映射"""
        print("正在从索引文件构建命令映射...")

        try:
            content = Config.INDEX_FILE.read_text(encoding="utf-8")
            lines = content.splitlines()

            # 正则表达式匹配命令链接
            # 格式: - [command_name](https://optics.ansys.com/hc/en-us/articles/{id}-{command})
            pattern = re.compile(
                r"- \[([^\]]+)\]\((https://optics\.ansys\.com/hc/en-us/articles/\d+-[^)]+)\)"
            )

            for line in lines:
                match = pattern.search(line)
                if match:
                    command_name = match.group(1).strip()
                    official_url = match.group(2).strip()

                    # 获取文件名
                    filename = FilenameEncoder.command_to_filename(command_name) + ".md"
                    local_path = f"./{filename}"

                    # 检查文件是否存在
                    filepath = Config.DOCS_EN_DIR / filename
                    if not filepath.exists():
                        print(f"警告: 命令 '{command_name}' 的文件不存在: {filename}")
                        continue

                    # 创建命令信息
                    cmd_info = CommandInfo(
                        name=command_name,
                        filename=filename,
                        official_url=official_url,
                        local_path=local_path,
                    )

                    self.commands[command_name] = cmd_info
                    self.filename_to_command[filename] = command_name

            print(f"成功映射 {len(self.commands)} 个命令")
            return True

        except Exception as e:
            print(f"构建命令映射失败: {e}")
            return False

    def get_command_info(self, command_name: str) -> Optional[CommandInfo]:
        """获取命令信息"""
        return self.commands.get(command_name)

    def get_command_by_filename(self, filename: str) -> Optional[str]:
        """通过文件名获取命令名"""
        return self.filename_to_command.get(filename)

    def get_all_commands(self) -> List[CommandInfo]:
        """获取所有命令信息"""
        return list(self.commands.values())

    def save_mapping(self, output_file: Path) -> bool:
        """保存映射到文件"""
        try:
            mapping = {
                "commands": {
                    name: info.to_dict() for name, info in self.commands.items()
                },
                "filename_to_command": self.filename_to_command,
                "timestamp": time.time(),
            }

            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(
                json.dumps(mapping, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            print(f"映射已保存到: {output_file}")
            return True
        except Exception as e:
            print(f"保存映射失败: {e}")
            return False

    def load_mapping(self, input_file: Path) -> bool:
        """从文件加载映射"""
        try:
            if not input_file.exists():
                print(f"映射文件不存在: {input_file}")
                return False

            data = json.loads(input_file.read_text(encoding="utf-8"))

            self.commands.clear()
            self.filename_to_command.clear()

            for name, info_dict in data.get("commands", {}).items():
                info = CommandInfo(**info_dict)
                self.commands[name] = info
                self.filename_to_command[info.filename] = name

            print(f"从文件加载了 {len(self.commands)} 个命令映射")
            return True
        except Exception as e:
            print(f"加载映射失败: {e}")
            return False


# ============================================================================
# 链接识别与转换
# ============================================================================


class LinkRecognizer:
    """链接识别器"""

    # 正则表达式模式
    PATTERNS = {
        # 命令文档链接: /hc/en-us/articles/{id}-{command}
        LinkType.COMMAND: re.compile(r"/hc/en-us/articles/(\d+)-([a-zA-Z0-9_-]+)"),
        # 命令列表链接
        LinkType.LIST_OF_COMMANDS: re.compile(r"/hc/en-us/articles/360037228834"),
        # 其他文章链接（非命令）
        LinkType.ARTICLE: re.compile(r"/hc/en-us/articles/(\d+)-[A-Z][a-zA-Z\s-]*"),
        # 锚点链接
        LinkType.ANCHOR: re.compile(r"#([a-zA-Z0-9_-]+)"),
        # 本地相对链接
        LinkType.LOCAL: re.compile(r"(\./|\.\./)[a-zA-Z0-9._-]+\.md"),
    }

    @staticmethod
    def identify_link(url: str, context: str = "") -> LinkType:
        """识别链接类型"""
        # 检查是否已经是完整URL
        if url.startswith("http://") or url.startswith("https://"):
            if "optics.ansys.com" in url:
                # 检查是否是命令链接
                if re.search(r"/hc/en-us/articles/\d+-[a-zA-Z0-9_-]+", url):
                    return LinkType.COMMAND
                elif Config.LIST_OF_COMMANDS_URL in url:
                    return LinkType.LIST_OF_COMMANDS
                else:
                    return LinkType.ARTICLE
            else:
                return LinkType.EXTERNAL

        # 检查相对路径
        if url.startswith("/hc/en-us/articles/"):
            if LinkRecognizer.PATTERNS[LinkType.LIST_OF_COMMANDS].search(url):
                return LinkType.LIST_OF_COMMANDS
            elif LinkRecognizer.PATTERNS[LinkType.COMMAND].search(url):
                return LinkType.COMMAND
            else:
                return LinkType.ARTICLE

        # 检查锚点
        if url.startswith("#"):
            return LinkType.ANCHOR

        # 检查本地文件
        if url.endswith(".md") and ("." in url or ".." in url):
            return LinkType.LOCAL

        # 未知类型
        return LinkType.EXTERNAL

    @staticmethod
    def extract_command_from_url(url: str) -> Optional[str]:
        """从URL中提取命令名"""
        if url.startswith("/hc/en-us/articles/"):
            match = LinkRecognizer.PATTERNS[LinkType.COMMAND].search(url)
            if match:
                return match.group(2)  # 命令名

        elif url.startswith("https://optics.ansys.com/hc/en-us/articles/"):
            # 从完整URL提取
            pattern = r"/hc/en-us/articles/\d+-([a-zA-Z0-9_-]+)"
            match = re.search(pattern, url)
            if match:
                return match.group(1)

        return None


class LinkConverter:
    """链接转换器"""

    def __init__(self, command_mapper: CommandMapper):
        self.command_mapper = command_mapper

    def convert_link(self, url: str, context: str = "") -> Tuple[str, LinkType]:
        """转换链接"""
        link_type = LinkRecognizer.identify_link(url, context)

        if link_type == LinkType.LIST_OF_COMMANDS:
            # 命令列表链接 → 本地索引文件
            return "../lsf-script-commands-alphabetical.md", link_type

        elif link_type == LinkType.COMMAND:
            # 命令文档链接 → 本地文件
            command_name = LinkRecognizer.extract_command_from_url(url)
            if command_name:
                cmd_info = self.command_mapper.get_command_info(command_name)
                if cmd_info:
                    return cmd_info.local_path, link_type

            # 如果无法映射，返回完整URL
            if url.startswith("/"):
                return Config.BASE_URL + url, link_type
            return url, link_type

        elif link_type == LinkType.ARTICLE:
            # 非命令文章链接 → 完整URL
            if url.startswith("/"):
                return Config.BASE_URL + url, link_type
            return url, link_type

        elif link_type == LinkType.LOCAL:
            # 本地链接保持不变
            return url, link_type

        elif link_type == LinkType.ANCHOR:
            # 锚点链接保持不变
            return url, link_type

        else:
            # 外部链接保持不变
            return url, link_type


# ============================================================================
# 文档处理器
# ============================================================================


class DocumentProcessor:
    """文档处理器"""

    def __init__(self, command_mapper: CommandMapper):
        self.command_mapper = command_mapper
        self.link_converter = LinkConverter(command_mapper)

        # Markdown链接模式
        self.link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    def process_file(self, filepath: Path) -> FileProcessingResult:
        """处理单个文档文件"""
        filename = filepath.name
        command_name = self.command_mapper.get_command_by_filename(filename)

        if not command_name:
            return FileProcessingResult(
                filename=filename,
                command_name="unknown",
                links_found=0,
                links_converted=0,
                formatting_success=False,
                error=f"无法识别命令名: {filename}",
            )

        try:
            # 读取文件
            content = filepath.read_text(encoding="utf-8")
            lines = content.splitlines()

            # 统计和转换链接
            links_found = 0
            links_converted = 0
            new_lines = []

            for i, line in enumerate(lines):
                new_line = line

                # 查找所有Markdown链接
                for match in self.link_pattern.finditer(line):
                    link_text = match.group(1)
                    original_url = match.group(2)
                    links_found += 1

                    # 转换链接
                    converted_url, link_type = self.link_converter.convert_link(
                        original_url, line
                    )

                    if original_url != converted_url:
                        links_converted += 1
                        # 替换链接
                        old_link = f"[{link_text}]({original_url})"
                        new_link = f"[{link_text}]({converted_url})"
                        new_line = new_line.replace(old_link, new_link)

                new_lines.append(new_line)

            # 写回文件
            new_content = "\n".join(new_lines)
            filepath.write_text(new_content, encoding="utf-8")

            # 格式化文件
            formatting_success = self._format_file(filepath)

            return FileProcessingResult(
                filename=filename,
                command_name=command_name,
                links_found=links_found,
                links_converted=links_converted,
                formatting_success=formatting_success,
                error=None,
            )

        except Exception as e:
            return FileProcessingResult(
                filename=filename,
                command_name=command_name,
                links_found=0,
                links_converted=0,
                formatting_success=False,
                error=str(e),
            )

    def _format_file(self, filepath: Path) -> bool:
        """使用mdformat格式化文件"""
        try:
            result = subprocess.run(
                [sys.executable, "-m", "mdformat", str(filepath), "--wrap", "88"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False


# ============================================================================
# 链接验证器（异步）
# ============================================================================


class LinkValidator:
    """异步链接验证器"""

    def __init__(self, max_concurrent: int = Config.MAX_CONCURRENT_REQUESTS):
        self.max_concurrent = max_concurrent
        self.session: Optional[Any] = None

    async def __aenter__(self):
        if HAS_AIOHTTP and aiohttp:
            self.session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=Config.REQUEST_TIMEOUT)
            )
        else:
            self.session = None
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session and HAS_AIOHTTP:
            await self.session.close()

    async def validate_link(self, url: str) -> ValidationResult:
        """验证单个链接"""
        if not self.session:
            return ValidationResult(
                url=url,
                status_code=None,
                error="Session not initialized",
                is_valid=False,
                response_time=0.0,
            )

        start_time = time.time()

        for attempt in range(Config.MAX_RETRIES):
            try:
                async with self.session.head(url, allow_redirects=True) as response:
                    response_time = time.time() - start_time
                    return ValidationResult(
                        url=url,
                        status_code=response.status,
                        error=None,
                        is_valid=response.status < 400,
                        response_time=response_time,
                    )
            except asyncio.TimeoutError:
                if attempt == Config.MAX_RETRIES - 1:
                    response_time = time.time() - start_time
                    return ValidationResult(
                        url=url,
                        status_code=None,
                        error=f"Timeout after {Config.REQUEST_TIMEOUT}s",
                        is_valid=False,
                        response_time=response_time,
                    )
                await asyncio.sleep(1)
            except Exception as e:
                response_time = time.time() - start_time
                return ValidationResult(
                    url=url,
                    status_code=None,
                    error=str(e),
                    is_valid=False,
                    response_time=response_time,
                )

        response_time = time.time() - start_time
        return ValidationResult(
            url=url,
            status_code=None,
            error="Max retries exceeded",
            is_valid=False,
            response_time=response_time,
        )

    async def validate_links_batch(self, urls: List[str]) -> List[ValidationResult]:
        """批量验证链接"""
        if not urls:
            return []

        semaphore = asyncio.Semaphore(self.max_concurrent)

        async def validate_with_semaphore(url: str) -> ValidationResult:
            async with semaphore:
                return await self.validate_link(url)

        tasks = [validate_with_semaphore(url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # 处理异常结果
        validated_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                validated_results.append(
                    ValidationResult(
                        url=urls[i],
                        status_code=None,
                        error=str(result),
                        is_valid=False,
                        response_time=0.0,
                    )
                )
            else:
                validated_results.append(result)

        return validated_results


# ============================================================================
# 索引文件转换器
# ============================================================================


class IndexTransformer:
    """索引文件转换器"""

    def __init__(self, command_mapper: CommandMapper):
        self.command_mapper = command_mapper

    def convert_to_table(self) -> str:
        """将索引文件转换为三列表格格式"""
        print("正在转换索引文件为表格格式...")

        try:
            # 从备份文件获取原始内容（用于提取Source行）
            backup_file = Config.BACKUP_DIR / "lsf-script-commands-alphabetical.md"
            original_source = "Source: https://optics.ansys.com/hc/en-us/articles/360034923553-Lumerical-scripting-language-Alphabetical-list"
            
            if backup_file.exists():
                backup_content = backup_file.read_text(encoding="utf-8")
                backup_lines = backup_content.splitlines()
                if len(backup_lines) > 2 and "https://" in backup_lines[2]:
                    original_source = backup_lines[2]
            
            # 读取当前索引文件内容（用于解析章节结构）
            content = Config.INDEX_FILE.read_text(encoding="utf-8")
            lines = content.splitlines()

            # 解析现有结构
            sections = self._parse_sections(lines)

            # 生成文档头部
            output_lines = [
                "# Lumerical Script Commands (Alphabetical)",
                "",
                original_source,  # 使用原始URL，而非本地路径
                "",
            ]

            for section_name, commands in sections.items():
                # 每个字母部分创建独立的表格
                output_lines.append(f"### {section_name}")
                output_lines.append("")
                output_lines.append("| 命令名 | 官方文档 | 本地文档 |")
                output_lines.append("|--------|----------|----------|")

                for command_name, url in commands:
                    cmd_info = self.command_mapper.get_command_info(command_name)
                    if cmd_info:
                        # 命令名链接到本地文件
                        command_cell = f"[{command_name}]({cmd_info.local_path})"
                        # 官方文档链接 - 使用"ANSYS"文字代替"链接"
                        official_cell = f"[ANSYS]({cmd_info.official_url})"
                        # 本地文档链接
                        local_cell = f"[{cmd_info.filename}]({cmd_info.local_path})"

                        output_lines.append(
                            f"| {command_cell} | {official_cell} | {local_cell} |"
                        )
                    else:
                        # 如果没有映射信息，只显示命令名
                        output_lines.append(f"| {command_name} | [ANSYS]({url}) | N/A |")

                output_lines.append("")  # 表格结束空行

            output_content = "\n".join(output_lines)
            return output_content

        except Exception as e:
            print(f"转换索引文件失败: {e}")
            return ""

    def _parse_sections(self, lines: List[str]) -> Dict[str, List[Tuple[str, str]]]:
        """解析现有的章节结构"""
        sections = {}
        current_section = None
        command_pattern = re.compile(r"- \[([^\]]+)\]\((https://[^)]+)\)")

        for line in lines:
            line = line.strip()

            # 检查是否是章节标题
            if line.startswith("## "):
                current_section = line[3:].strip()
                sections[current_section] = []
            elif line.startswith("- [") and current_section:
                match = command_pattern.search(line)
                if match:
                    command_name = match.group(1).strip()
                    url = match.group(2).strip()
                    sections[current_section].append((command_name, url))

        return sections

    def save_converted_index(self, output_path: Optional[Path] = None) -> bool:
        """保存转换后的索引文件"""
        if output_path is None:
            output_path = Config.INDEX_FILE

        try:
            table_content = self.convert_to_table()
            if not table_content:
                return False

            # 备份原文件
            backup_path = output_path.with_suffix(".md.backup")
            if output_path.exists():
                output_path.rename(backup_path)

            # 写入新内容
            output_path.write_text(table_content, encoding="utf-8")

            print(f"索引文件已转换为表格格式: {output_path}")
            return True

        except Exception as e:
            print(f"保存转换后的索引文件失败: {e}")
            return False


# ============================================================================
# 检查点管理器
# ============================================================================


class CheckpointManager:
    """检查点管理器（支持断点续传）"""

    def __init__(self):
        self.checkpoint_file = Config.CHECKPOINT_FILE
        self.data = {
            "start_time": time.time(),
            "total_files": 0,
            "processed_files": 0,
            "failed_files": [],
            "current_batch": 0,
            "last_successful_file": None,
            "completed": False,
        }

    def load(self) -> bool:
        """加载检查点"""
        try:
            if self.checkpoint_file.exists():
                self.data = json.loads(self.checkpoint_file.read_text(encoding="utf-8"))
                print(
                    f"从检查点恢复: 已处理 {self.data['processed_files']}/{self.data['total_files']} 个文件"
                )
                return True
            return False
        except Exception as e:
            print(f"加载检查点失败: {e}")
            return False

    def save(self) -> bool:
        """保存检查点"""
        try:
            self.checkpoint_file.parent.mkdir(parents=True, exist_ok=True)
            self.checkpoint_file.write_text(
                json.dumps(self.data, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            return True
        except Exception as e:
            print(f"保存检查点失败: {e}")
            return False

    def update(self, filename: str, success: bool = True):
        """更新检查点"""
        self.data["processed_files"] += 1

        if success:
            self.data["last_successful_file"] = filename
        else:
            self.data["failed_files"].append(filename)

        self.save()

    def mark_completed(self):
        """标记任务完成"""
        self.data["completed"] = True
        self.data["end_time"] = time.time()
        self.save()

    def get_remaining_files(self, all_files: List[str]) -> List[str]:
        """获取剩余待处理的文件"""
        if not self.data.get("last_successful_file"):
            return all_files

        try:
            last_index = all_files.index(self.data["last_successful_file"])
            return all_files[last_index + 1 :]
        except ValueError:
            return all_files

    def clear(self):
        """清除检查点"""
        if self.checkpoint_file.exists():
            self.checkpoint_file.unlink()


# ============================================================================
# 报告生成器
# ============================================================================


class ReportGenerator:
    """报告生成器"""

    def __init__(self):
        self.report_file = Config.REPORT_FILE
        self.report_data = {
            "summary": {
                "total_files": 0,
                "processed_files": 0,
                "successful_files": 0,
                "failed_files": 0,
                "links_updated": 0,
                "formatting_errors": 0,
                "validation_errors": 0,
                "start_time": None,
                "end_time": None,
                "duration_seconds": 0,
            },
            "details": {"file_results": [], "validation_results": [], "errors": []},
        }

    def start(self, total_files: int):
        """开始记录"""
        self.report_data["summary"]["total_files"] = total_files
        self.report_data["summary"]["start_time"] = time.time()

    def add_file_result(self, result: FileProcessingResult):
        """添加文件处理结果"""
        self.report_data["details"]["file_results"].append(result.to_dict())
        self.report_data["summary"]["processed_files"] += 1

        if result.error:
            self.report_data["summary"]["failed_files"] += 1
            self.report_data["details"]["errors"].append(
                {"file": result.filename, "error": result.error}
            )
        else:
            self.report_data["summary"]["successful_files"] += 1

        self.report_data["summary"]["links_updated"] += result.links_converted

        if not result.formatting_success:
            self.report_data["summary"]["formatting_errors"] += 1

    def add_validation_results(self, results: List[ValidationResult]):
        """添加验证结果"""
        for result in results:
            self.report_data["details"]["validation_results"].append(result.to_dict())
            if not result.is_valid:
                self.report_data["summary"]["validation_errors"] += 1

    def finish(self):
        """完成报告"""
        end_time = time.time()
        start_time = self.report_data["summary"].get("start_time", end_time)

        self.report_data["summary"]["end_time"] = end_time
        self.report_data["summary"]["duration_seconds"] = end_time - start_time

    def save(self):
        """保存报告"""
        try:
            self.report_file.parent.mkdir(parents=True, exist_ok=True)
            self.report_file.write_text(
                json.dumps(self.report_data, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            print(f"报告已保存到: {self.report_file}")
            return True
        except Exception as e:
            print(f"保存报告失败: {e}")
            return False

    def print_summary(self):
        """打印摘要"""
        summary = self.report_data["summary"]

        print("\n" + "=" * 60)
        print("文档优化任务摘要")
        print("=" * 60)
        print(f"总文件数: {summary['total_files']}")
        print(f"成功处理: {summary['successful_files']}")
        print(f"失败文件: {summary['failed_files']}")
        print(f"链接更新: {summary['links_updated']}")
        print(f"格式化错误: {summary['formatting_errors']}")
        print(f"验证错误: {summary['validation_errors']}")

        if summary["duration_seconds"] > 0:
            duration_min = summary["duration_seconds"] / 60
            print(f"总耗时: {duration_min:.1f} 分钟")
        print("=" * 60)


# ============================================================================
# 主优化器
# ============================================================================


class DocumentationOptimizer:
    """文档优化器主类"""

    def __init__(self):
        self.command_mapper = CommandMapper()
        self.checkpoint_manager = CheckpointManager()
        self.report_generator = ReportGenerator()

        # 进度跟踪
        self.progress_file = Config.PROGRESS_FILE

    def run(self, resume: bool = True) -> bool:
        """运行优化任务"""
        print("=" * 60)
        print("Lumerical 文档质量优化任务")
        print("=" * 60)

        # 构建命令映射
        if not self.command_mapper.build_from_index():
            print("错误: 无法构建命令映射")
            return False

        # 获取所有文件
        all_files = sorted(
            [f.name for f in Config.DOCS_EN_DIR.glob("*.md") if f.is_file()]
        )

        if not all_files:
            print("错误: 未找到文档文件")
            return False

        print(f"找到 {len(all_files)} 个文档文件")

        # 加载检查点（断点续传）
        remaining_files = all_files
        if resume and self.checkpoint_manager.load():
            remaining_files = self.checkpoint_manager.get_remaining_files(all_files)
            print(f"从检查点恢复: 剩余 {len(remaining_files)} 个文件待处理")

        # 初始化报告
        self.report_generator.start(len(all_files))

        # 分批处理
        batch_size = Config.BATCH_SIZE
        total_batches = (len(remaining_files) + batch_size - 1) // batch_size

        success = True
        processor = DocumentProcessor(self.command_mapper)

        for batch_idx in range(total_batches):
            start_idx = batch_idx * batch_size
            end_idx = min(start_idx + batch_size, len(remaining_files))
            batch_files = remaining_files[start_idx:end_idx]

            print(
                f"\n处理批次 {batch_idx + 1}/{total_batches} ({len(batch_files)} 个文件)..."
            )

            for filename in batch_files:
                filepath = Config.DOCS_EN_DIR / filename

                print(f"  处理: {filename}", end="", flush=True)

                result = processor.process_file(filepath)
                self.report_generator.add_file_result(result)
                self.checkpoint_manager.update(filename, result.error is None)

                if result.error:
                    print(f" [FAIL] 错误: {result.error}")
                    success = False
                else:
                    print(
                        f" [OK] 已更新 {result.links_converted}/{result.links_found} 个链接"
                    )

        # 转换索引文件
        print("\n转换索引文件...")
        transformer = IndexTransformer(self.command_mapper)
        if transformer.save_converted_index():
            print("索引文件转换成功")
        else:
            print("索引文件转换失败")
            success = False

        # 完成检查点和报告
        self.checkpoint_manager.mark_completed()
        self.report_generator.finish()
        self.report_generator.save()
        self.report_generator.print_summary()

        return success

    async def validate_links(self) -> bool:
        """验证所有外部链接"""
        print("\n" + "=" * 60)
        print("验证外部链接有效性")
        print("=" * 60)

        # 检查aiohttp是否可用
        if not HAS_AIOHTTP:
            print("警告: aiohttp 未安装，跳过链接验证")
            print("请安装 aiohttp: pip install aiohttp 或 uv add aiohttp")
            return True

        # 收集所有外部链接
        external_links = self._collect_external_links()

        if not external_links:
            print("未找到需要验证的外部链接")
            return True

        print(f"找到 {len(external_links)} 个外部链接需要验证")

        # 异步验证
        async with LinkValidator() as validator:
            print("开始验证链接...")
            results = await validator.validate_links_batch(external_links)

        # 统计结果
        valid_count = sum(1 for r in results if r.is_valid)
        invalid_count = len(results) - valid_count

        print(f"验证完成: {valid_count} 个有效, {invalid_count} 个无效")

        # 保存验证结果到报告
        self.report_generator.add_validation_results(results)
        self.report_generator.save()

        # 显示无效链接
        if invalid_count > 0:
            print("\n无效链接:")
            for result in results:
                if not result.is_valid:
                    print(f"  [FAIL] {result.url}")
                    if result.error:
                        print(f"     错误: {result.error}")

        return invalid_count == 0

    def _collect_external_links(self) -> List[str]:
        """收集所有外部链接"""
        external_links = set()
        link_converter = LinkConverter(self.command_mapper)

        for filepath in Config.DOCS_EN_DIR.glob("*.md"):
            content = filepath.read_text(encoding="utf-8")

            # 查找所有Markdown链接
            for match in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", content):
                url = match.group(2)

                # 转换链接以确定类型
                converted_url, link_type = link_converter.convert_link(url)

                # 只收集外部链接（非本地、非锚点）
                if link_type not in [LinkType.LOCAL, LinkType.ANCHOR]:
                    if link_type == LinkType.COMMAND and converted_url.startswith("./"):
                        # 本地命令链接，跳过
                        continue
                    elif (
                        link_type == LinkType.LIST_OF_COMMANDS
                        and converted_url == "../lsf-script-commands-alphabetical.md"
                    ):
                        # 本地索引链接，跳过
                        continue
                    else:
                        # 外部链接
                        external_links.add(converted_url)

        return list(external_links)


# ============================================================================
# 命令行接口
# ============================================================================


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="Lumerical文档质量优化工具")
    parser.add_argument(
        "--resume", action="store_true", default=True, help="启用断点续传（默认启用）"
    )
    parser.add_argument(
        "--no-resume", action="store_false", dest="resume", help="禁用断点续传"
    )
    parser.add_argument("--validate", action="store_true", help="验证外部链接有效性")
    parser.add_argument("--clean", action="store_true", help="清理检查点和临时文件")

    args = parser.parse_args()

    # 清理模式
    if args.clean:
        print("清理检查点和临时文件...")
        checkpoint_files = [
            Config.CHECKPOINT_FILE,
            Config.PROGRESS_FILE,
            Config.ERROR_LOG,
            Config.REPORT_FILE,
        ]

        for file in checkpoint_files:
            if file.exists():
                file.unlink()
                print(f"已删除: {file}")

        print("清理完成")
        return 0

    # 运行优化器
    optimizer = DocumentationOptimizer()

    try:
        # 执行优化
        if not optimizer.run(resume=args.resume):
            print("优化任务失败")
            return 1

        # 验证链接（如果指定）
        if args.validate:
            loop = asyncio.get_event_loop()
            if not loop.run_until_complete(optimizer.validate_links()):
                print("链接验证发现无效链接")
                return 1

        print("\n[SUCCESS] 文档优化任务完成!")
        return 0

    except KeyboardInterrupt:
        print("\n[WARN] 任务被用户中断")
        print("下次运行可以使用 --resume 参数从断点继续")
        return 130
    except Exception as e:
        print(f"\n[FAIL] 发生错误: {e}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
