#!/usr/bin/env python3
"""
增量抓取缺失的LSF脚本命令文档。
从missing-commands.json读取缺失命令列表，每分钟尝试抓取一个。
成功抓取后从列表中删除，失败则记录并等待2分钟尝试下一个。
"""

import json
import logging
import time
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
FAILED_COMMANDS_FILE = Path(__file__).parent.parent / "docs" / "failed-commands.json"
PROGRESS_FILE = Path(__file__).parent.parent / "docs" / "scrape-progress.json"
SLEEP_SUCCESS = 60  # 成功抓取后等待60秒
SLEEP_FAILURE = 120  # 失败后等待120秒
MAX_RETRIES = 3  # 每个命令最大重试次数
DRY_RUN = False  # 设置为True以进行干跑测试，不实际抓取
MAX_COMMANDS = 1  # 最大处理命令数，设为1以稳定抓取

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(Path(__file__).parent.parent / "docs" / "scrape.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def load_missing_commands() -> list[tuple[str, str]]:
    """从missing-lsf-script-docs.md加载缺失命令列表。"""
    import re

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
        if commands:
            logger.info(f"示例命令: {commands[:3]}")
        return commands
    except Exception as e:
        logger.error(f"加载缺失命令文件失败: {e}", exc_info=True)
        return []


def load_progress() -> dict:
    """加载进度文件，记录已处理命令和失败计数。"""
    if PROGRESS_FILE.exists():
        try:
            with open(PROGRESS_FILE, encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"加载进度文件失败: {e}")
    return {
        "processed": [],  # 已成功处理的命令
        "failed": {},  # 失败命令及其重试次数，例如 {"command": 2}
        "last_command": None,
    }


def save_progress(progress: dict):
    """保存进度文件。"""
    if DRY_RUN:
        logger.debug("干跑模式: 跳过保存进度")
        return
    try:
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump(progress, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"保存进度文件失败: {e}")


def update_missing_commands(remaining_commands: list[tuple[str, str]]):
    """
    更新missing-lsf-script-docs.md文件，移除已处理的命令。
    """
    if DRY_RUN:
        logger.info(
            f"干跑模式: 将更新缺失命令文件，剩余 {len(remaining_commands)} 个命令。"
        )
        return
    try:
        import re

        content = MISSING_COMMANDS_FILE.read_text(encoding="utf-8")
        lines = content.splitlines()
        remaining_set = {cmd for cmd, _ in remaining_commands}
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
                    if cmd in remaining_set:
                        new_lines.append(line)
                    else:
                        logger.debug(f"移除命令行: {cmd}")
                        continue
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        new_content = "\n".join(new_lines)
        MISSING_COMMANDS_FILE.write_text(new_content, encoding="utf-8")
        logger.info(
            f"更新缺失命令Markdown文件，剩余 {len(remaining_commands)} 个命令。"
        )
    except Exception as e:
        logger.error(f"更新缺失命令文件失败: {e}")


def record_failed_command(command: str, url: str, progress: dict):
    """记录失败命令，增加重试计数。"""
    failed = progress.get("failed", {})
    count = failed.get(command, 0) + 1
    failed[command] = count
    progress["failed"] = failed
    logger.warning(f"命令 {command} 抓取失败，重试次数 {count}/{MAX_RETRIES}")

    # 如果达到最大重试次数，将其从待处理列表中移除（避免无限重试）
    if count >= MAX_RETRIES:
        logger.error(f"命令 {command} 已达到最大重试次数，将被标记为永久失败。")
        if DRY_RUN:
            logger.info("干跑模式: 跳过保存永久失败命令")
            return
        # 可以保存到单独文件
        try:
            failed_data = {}
            if FAILED_COMMANDS_FILE.exists():
                with open(FAILED_COMMANDS_FILE, encoding="utf-8") as f:
                    failed_data = json.load(f)
            failed_commands = failed_data.get("permanent_failures", [])
            failed_commands.append([command, url])
            failed_data["permanent_failures"] = failed_commands
            with open(FAILED_COMMANDS_FILE, "w", encoding="utf-8") as f:
                json.dump(failed_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"保存永久失败命令失败: {e}")


def scrape_command(command: str, url: str) -> bool:
    """抓取单个命令文档，成功返回True。"""
    logger.info(f"开始抓取命令: {command}")
    if DRY_RUN:
        logger.info(f"干跑模式: 模拟成功抓取 {command}")
        return True
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


def main():
    logger.info("=" * 60)
    logger.info("LSF缺失文档增量抓取启动")
    logger.info(f"缺失命令文件: {MISSING_COMMANDS_FILE}")
    logger.info(f"输出目录: {OUTPUT_DIR}")
    logger.info(f"成功等待: {SLEEP_SUCCESS}秒, 失败等待: {SLEEP_FAILURE}秒")
    logger.info("=" * 60)

    # 加载缺失命令列表
    missing_commands = load_missing_commands()
    if not missing_commands:
        logger.warning("没有缺失命令需要抓取。")
        return

    logger.info(f"共发现 {len(missing_commands)} 个缺失命令。")

    # 加载进度
    progress = load_progress()
    processed = set(progress.get("processed", []))
    failed_counts = progress.get("failed", {})
    logger.info(f"已处理命令数: {len(processed)}")
    logger.info(f"失败计数: {failed_counts}")

    # 过滤掉已处理的命令
    remaining_commands = []
    for cmd_name, cmd_url in missing_commands:
        if cmd_name in processed:
            logger.debug(f"跳过已处理命令: {cmd_name}")
            continue
        # 检查是否已达到最大重试次数
        if failed_counts.get(cmd_name, 0) >= MAX_RETRIES:
            logger.warning(f"跳过已达到最大重试次数的命令: {cmd_name}")
            continue
        remaining_commands.append((cmd_name, cmd_url))

    logger.info(f"剩余待抓取命令: {len(remaining_commands)} 个")

    # 如果没有待处理命令，退出
    if not remaining_commands:
        logger.info("没有待抓取的命令。")
        return

    # 主循环
    for idx, (cmd_name, cmd_url) in enumerate(remaining_commands):
        if MAX_COMMANDS and idx >= MAX_COMMANDS:
            logger.info(f"达到最大处理命令数 {MAX_COMMANDS}，停止处理。")
            break
        logger.info(f"处理命令 {idx + 1}/{len(remaining_commands)}: {cmd_name}")

        success = scrape_command(cmd_name, cmd_url)

        if success:
            # 记录为已处理
            processed.add(cmd_name)
            progress["processed"] = list(processed)
            # 从失败计数中移除（如果存在）
            failed_counts.pop(cmd_name, None)
            progress["failed"] = failed_counts
            # 从剩余命令列表中移除（在循环结束后统一更新文件）
            # 更新进度文件
            save_progress(progress)
            # 等待成功间隔
            if idx < len(remaining_commands) - 1:  # 不是最后一个
                if not DRY_RUN:
                    logger.info(f"等待 {SLEEP_SUCCESS} 秒后处理下一个命令...")
                    time.sleep(SLEEP_SUCCESS)
                else:
                    logger.info("干跑模式: 跳过等待")
        else:
            # 记录失败
            record_failed_command(cmd_name, cmd_url, progress)
            # 更新失败计数
            failed_counts = progress.get("failed", {})
            # 保存进度
            save_progress(progress)
            # 等待失败间隔
            if idx < len(remaining_commands) - 1:
                if not DRY_RUN:
                    logger.info(f"抓取失败，等待 {SLEEP_FAILURE} 秒后尝试下一个命令...")
                    time.sleep(SLEEP_FAILURE)
                else:
                    logger.info("干跑模式: 跳过等待")

    # 更新缺失命令文件（移除已处理的命令）
    # 重新计算剩余命令（包括失败的但未达到最大重试次数的）
    final_remaining = []
    for cmd_name, cmd_url in missing_commands:
        if cmd_name in processed:
            continue
        if failed_counts.get(cmd_name, 0) >= MAX_RETRIES:
            continue
        final_remaining.append((cmd_name, cmd_url))

    update_missing_commands(final_remaining)

    logger.info("=" * 60)
    logger.info("抓取任务完成")
    logger.info(f"成功处理: {len(processed)} 个命令")
    logger.info(f"剩余缺失: {len(final_remaining)} 个命令")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
