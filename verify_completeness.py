#!/usr/bin/env python3
"""验证LSF命令文档完整性"""

import re
import json
from pathlib import Path
from typing import List, Tuple, Set

# 配置文件
INDEX_FILE = Path(__file__).parent / "docs" / "lsf-script-commands-alphabetical.md"
OUTPUT_DIR = Path(__file__).parent / "docs" / "lsf-script"


def parse_index_file() -> List[Tuple[str, str]]:
    """解析索引文件，提取所有命令和URL。"""
    commands = []
    # 改进的正则表达式，处理命令名中包含方括号的情况
    pattern = re.compile(r"- \[([^\]]*?)\]\(([^)]+)\)")

    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    matches = pattern.findall(content)
    for cmd_name, cmd_url in matches:
        commands.append((cmd_name.strip(), cmd_url.strip()))

    return commands


def sanitize_filename(name: str) -> str:
    """将命令名转换为安全的文件名（与抓取脚本使用相同的逻辑）。"""
    original_name = name

    # 替换Windows文件名中的非法字符
    illegal_chars = r'<>:"/\\|?*'
    for char in illegal_chars:
        name = name.replace(char, "_")

    # 替换其他可能有问题字符
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

    # 如果文件名仍然以点开头，添加前缀
    if name.startswith("."):
        name = "dot" + name

    # 如果文件名为空或太长，使用哈希
    if not name:
        import hashlib

        name = hashlib.md5(original_name.encode()).hexdigest()[:8]

    return name


def get_existing_files() -> Set[str]:
    """获取已存在的Markdown文件名集合（不包含扩展名）。"""
    existing_files = set()
    for md_file in OUTPUT_DIR.glob("*.md"):
        # 去掉扩展名
        existing_files.add(md_file.stem)
    return existing_files


def main():
    print("验证LSF命令文档完整性...")
    print("=" * 60)

    # 解析索引文件
    commands = parse_index_file()
    print(f"索引文件中的命令总数: {len(commands)}")

    # 获取现有文件
    existing_files = get_existing_files()
    print(f"现有文档文件数: {len(existing_files)}")

    # 计算缺失命令
    missing_commands = []
    for cmd_name, cmd_url in commands:
        sanitized_name = sanitize_filename(cmd_name)
        if sanitized_name not in existing_files:
            missing_commands.append((cmd_name, cmd_url, sanitized_name))

    print(f"缺失命令数: {len(missing_commands)}")

    if missing_commands:
        print("\n缺失的命令:")
        for cmd_name, cmd_url, sanitized_name in missing_commands[:20]:  # 最多显示20个
            print(f"  - {cmd_name} -> {sanitized_name}.md")
        if len(missing_commands) > 20:
            print(f"  ... 还有 {len(missing_commands) - 20} 个缺失命令")
    else:
        print("\n[SUCCESS] 所有命令文档已完整抓取！")

    # 检查重复的文件名（多个命令映射到同一个文件名）
    cmd_to_file = {}
    duplicates = []
    for cmd_name, cmd_url in commands:
        sanitized_name = sanitize_filename(cmd_name)
        if sanitized_name in cmd_to_file:
            duplicates.append((sanitized_name, cmd_name, cmd_to_file[sanitized_name]))
        else:
            cmd_to_file[sanitized_name] = cmd_name

    if duplicates:
        print(f"\n[WARNING] 发现 {len(duplicates)} 个文件名冲突:")
        for sanitized_name, cmd1, cmd2 in duplicates[:10]:
            print(f"  - {sanitized_name}.md: {cmd1} 和 {cmd2}")

    print("=" * 60)

    # 保存结果到文件
    result_file = Path(__file__).parent / "docs" / "verification-result.md"
    with open(result_file, "w", encoding="utf-8") as f:
        f.write("# LSF命令文档验证结果\n\n")
        f.write(f"**验证时间**: 2026-02-02\n")
        f.write(f"**索引文件**: `{INDEX_FILE.name}`\n")
        f.write(f"**文档目录**: `{OUTPUT_DIR.name}`\n\n")
        f.write("## 统计\n\n")
        f.write(f"- **总命令数**: {len(commands)}\n")
        f.write(f"- **现有文档数**: {len(existing_files)}\n")
        f.write(f"- **缺失命令数**: {len(missing_commands)}\n")
        f.write(f"- **完成率**: {(len(existing_files) / len(commands)) * 100:.1f}%\n\n")

        if missing_commands:
            f.write("## 缺失命令列表\n\n")
            f.write("| 命令名 | 清理后文件名 | URL |\n")
            f.write("|--------|--------------|-----|\n")
            for cmd_name, cmd_url, sanitized_name in missing_commands:
                f.write(f"| `{cmd_name}` | `{sanitized_name}.md` | {cmd_url} |\n")

    print(f"详细结果已保存到: {result_file}")


if __name__ == "__main__":
    main()
