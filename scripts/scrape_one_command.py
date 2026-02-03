#!/usr/bin/env python3
"""
单次抓取LSF脚本命令文档。
用法:
  python scrape_one_command.py                    # 显示缺失命令列表
  python scrape_one_command.py "command_name"     # 抓取指定命令
  python scrape_one_command.py --next             # 抓取下一个缺失命令
"""

import argparse
import json
import logging
import re
from pathlib import Path

# Markdown formatting configuration
ENABLE_MARKDOWN_FORMAT = True  # 是否启用Markdown格式化

# 尝试从现有脚本导入抓取函数
try:
    from update_lsf_docs_resume import (
        OUTPUT_DIR,
        extract_command_content,
        fetch_page,
        sanitize_filename,
        save_command_markdown,
    )

    HAVE_SCRAPER_FUNCS = True
except ImportError as e:
    logging.warning(f"无法导入现有抓取函数: {e}")
    HAVE_SCRAPER_FUNCS = False
    # 定义占位函数，实际使用时需要实现
    OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "lsf-script" / "en"

    def fetch_page(url: str) -> str | None:
        logging.error("fetch_page 未实现，请确保依赖已安装")
        return None

    def extract_command_content(html: str, command_name: str) -> str:
        return f"# {command_name}\n\n文档内容抓取失败。"

    def format_markdown_file(filepath: Path) -> bool:
        """Format a markdown file using mdformat with tables plugin.
        
        Returns True if formatting succeeded or was skipped, False on error.
        """
        if not ENABLE_MARKDOWN_FORMAT:
            return True
        try:
            import subprocess
            import sys
            
            # 使用mdformat命令行工具格式化文件
            result = subprocess.run(
                [sys.executable, "-m", "mdformat", str(filepath), "--wrap", "88"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                logging.warning(f"mdformat failed for {filepath}: {result.stderr}")
                return False
            logging.info(f"Formatted {filepath}")
            return True
        except Exception as e:
            logging.warning(f"Error formatting {filepath}: {e}")
            return False

    def save_command_markdown(command_name: str, content: str):
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        filename = sanitize_filename(command_name)
        filepath = OUTPUT_DIR / f"{filename}.md"
        filepath.write_text(content, encoding="utf-8")
        logging.info(f"保存 {command_name} -> {filepath}")
        
        # 格式化Markdown文件
        format_markdown_file(filepath)

    def sanitize_filename(name: str) -> str:
        original_name = name  # 保存原始名称用于哈希

        # 多字符组合替换 - 先执行，避免被单字符替换拆散
        multi_char_replacements = {
            "<=": "lte",
            ">=": "gte",
            "==": "equalequal",
            "!=": "notequal",
            "+=": "plusequals",
            "-=": "minusequals",
            "*=": "asteriskequals",
            "/=": "slashequals",
        }
        for combo, replacement in multi_char_replacements.items():
            name = name.replace(combo, replacement)

        # 替换其他可能有问题字符 - 先执行这个，确保特殊字符被正确替换
        replacements = {
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

        for char, replacement in replacements.items():
            name = name.replace(char, replacement)

        # 然后替换Windows文件名中的非法字符（可能已被替换）
        illegal_chars = r'<>:"/\\|?*'
        for char in illegal_chars:
            name = name.replace(char, "_")

        # 如果文件名仍然以点开头，添加前缀
        if name.startswith("."):
            name = "dot" + name

        # 如果文件名为空或太长，使用哈希
        if not name:
            import hashlib

            name = hashlib.md5(original_name.encode()).hexdigest()[:8]

        return name


# 配置
MISSING_COMMANDS_FILE = (
    Path(__file__).parent.parent / "docs" / "missing-lsf-script-docs.md"
)
PROGRESS_FILE = Path(__file__).parent.parent / "docs" / "scrape-progress.json"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(
            Path(__file__).parent.parent / "docs" / "scrape-single.log"
        ),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def load_missing_commands() -> list[tuple[str, str]]:
    """从missing-lsf-script-docs.md加载缺失命令列表。"""
    try:
        logger.info(f"加载Markdown文件: {MISSING_COMMANDS_FILE}")
        content = MISSING_COMMANDS_FILE.read_text(encoding="utf-8")
        # 正则表达式匹配表格行： | "command" | [url](url) |
        pattern = r'^\|\s*"([^"]+)"\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|'
        commands = []
        for line in content.splitlines():
            line = line.strip()
            if not line.startswith("|"):
                continue
            match = re.search(pattern, line)
            if match:
                cmd = match.group(1).strip()
                # URL在方括号内，但实际URL在group(3)（链接目标）
                url = match.group(3).strip()
                commands.append((cmd, url))
        logger.info(f"从Markdown文件解析了 {len(commands)} 个命令")
        return commands
    except Exception as e:
        logger.error(f"加载缺失命令文件失败: {e}", exc_info=True)
        return []


def load_progress() -> dict:
    """加载进度文件，记录已处理命令。"""
    if PROGRESS_FILE.exists():
        try:
            with open(PROGRESS_FILE, encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"加载进度文件失败: {e}")
    return {
        "processed": [],  # 已成功处理的命令
        "last_command": None,
    }


def save_progress(progress: dict):
    """保存进度文件。"""
    try:
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump(progress, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"保存进度文件失败: {e}")


def remove_command_from_missing(command: str):
    """从缺失命令文件中移除指定命令。"""
    try:
        import re

        content = MISSING_COMMANDS_FILE.read_text(encoding="utf-8")
        lines = content.splitlines()
        new_lines = []
        table_pattern = re.compile(
            r'^\|\s*"([^"]+)"\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|'
        )
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("|") and '"' in stripped:
                match = table_pattern.match(stripped)
                if match:
                    cmd = match.group(1).strip()
                    if cmd == command:
                        logger.debug(f"移除命令行: {cmd}")
                        continue
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        new_content = "\n".join(new_lines)
        MISSING_COMMANDS_FILE.write_text(new_content, encoding="utf-8")
        logger.info(f"从缺失命令列表中移除: {command}")
    except Exception as e:
        logger.error(f"更新缺失命令文件失败: {e}")


def scrape_command(command: str, url: str) -> bool:
    """抓取单个命令文档，成功返回True。"""
    logger.info(f"开始抓取命令: {command}")
    if not HAVE_SCRAPER_FUNCS:
        logger.error("抓取函数未正确导入，请检查依赖安装")
        return False

    try:
        html = fetch_page(url)
        if not html:
            logger.error(f"无法获取页面内容: {command}")
            return False

        content = extract_command_content(html, command)
        save_command_markdown(command, content)
        logger.info(f"成功抓取命令: {command}")
        return True
    except Exception as e:
        logger.error(f"抓取命令 {command} 时发生异常: {e}")
        return False


def display_missing_commands():
    """显示缺失命令列表。"""
    commands = load_missing_commands()
    if not commands:
        print("没有缺失命令需要抓取。")
        return

    print(f"缺失命令总数: {len(commands)}")
    print("\n前20个缺失命令:")
    for i, (cmd, _url) in enumerate(commands[:20]):
        print(f"  {i + 1:3d}. {cmd}")

    progress = load_progress()
    processed = set(progress.get("processed", []))
    remaining = [cmd for cmd, _ in commands if cmd not in processed]
    print(f"\n剩余待抓取命令数: {len(remaining)}")


def get_next_command() -> tuple[str, str] | None:
    """获取下一个待抓取命令。"""
    commands = load_missing_commands()
    if not commands:
        return None

    progress = load_progress()
    processed = set(progress.get("processed", []))

    for cmd, url in commands:
        if cmd not in processed:
            return cmd, url

    return None


def main():
    parser = argparse.ArgumentParser(description="单次抓取LSF脚本命令文档")
    parser.add_argument(
        "command", nargs="?", help="要抓取的命令名称（如：'addport (FDTD)'）"
    )
    parser.add_argument("--next", action="store_true", help="抓取下一个缺失命令")
    parser.add_argument("--list", action="store_true", help="显示缺失命令列表")
    parser.add_argument("--stats", action="store_true", help="显示统计信息")

    args = parser.parse_args()

    if args.list:
        display_missing_commands()
        return

    if args.stats:
        commands = load_missing_commands()
        progress = load_progress()
        processed = set(progress.get("processed", []))
        remaining = [cmd for cmd, _ in commands if cmd not in processed]
        print(f"缺失命令总数: {len(commands)}")
        print(f"已处理命令数: {len(processed)}")
        print(f"剩余命令数: {len(remaining)}")
        return

    # 确定要抓取的命令
    target_command = None
    target_url = None

    if args.command:
        # 用户指定的命令
        commands = load_missing_commands()
        for cmd, url in commands:
            if cmd == args.command:
                target_command = cmd
                target_url = url
                break

        if not target_command:
            print(f"错误: 命令 '{args.command}' 不在缺失命令列表中")
            print("请使用 --list 查看可用命令")
            return
    elif args.next:
        # 抓取下一个命令
        result = get_next_command()
        if result:
            target_command, target_url = result
        else:
            print("没有待抓取的命令")
            return
    else:
        # 没有参数，显示帮助和列表
        display_missing_commands()
        print("\n用法:")
        print('  python scrape_one_command.py "command_name"  # 抓取指定命令')
        print("  python scrape_one_command.py --next           # 抓取下一个命令")
        print("  python scrape_one_command.py --list           # 显示命令列表")
        return

    # 执行抓取
    print(f"准备抓取命令: {target_command}")
    print(f"URL: {target_url}")

    if not target_url:
        print(f"错误: 命令 '{target_command}' 没有对应的URL")
        return

    success = scrape_command(target_command, target_url)

    # 更新进度
    if success:
        progress = load_progress()
        processed = set(progress.get("processed", []))
        processed.add(target_command)
        progress["processed"] = list(processed)
        progress["last_command"] = target_command
        save_progress(progress)

        # 从缺失列表中移除
        remove_command_from_missing(target_command)

        print(f"[SUCCESS] 成功抓取命令: {target_command}")
        print("[SUCCESS] 已从缺失列表中移除")
    else:
        print(f"[FAILED] 抓取失败: {target_command}")
        print("请检查网络连接或稍后重试")

    # 显示剩余命令数
    commands = load_missing_commands()
    progress = load_progress()
    processed = set(progress.get("processed", []))
    remaining = [cmd for cmd, _ in commands if cmd not in processed]
    print(f"\n剩余待抓取命令数: {len(remaining)}")


if __name__ == "__main__":
    main()
