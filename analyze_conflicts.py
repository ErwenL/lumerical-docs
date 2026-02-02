#!/usr/bin/env python3
"""分析文件名冲突"""

import re
from pathlib import Path
from collections import defaultdict

# 配置文件
INDEX_FILE = Path(__file__).parent / "docs" / "lsf-script-commands-alphabetical.md"
OUTPUT_DIR = Path(__file__).parent / "docs" / "lsf-script"


def parse_index_file():
    """解析索引文件，提取所有命令和URL。"""
    commands = []
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


def main():
    commands = parse_index_file()
    print(f"总命令数: {len(commands)}")

    # 按清理后的文件名分组
    file_to_commands = defaultdict(list)
    for cmd_name, cmd_url in commands:
        sanitized = sanitize_filename(cmd_name)
        file_to_commands[sanitized].append((cmd_name, cmd_url))

    # 找出冲突
    conflicts = {f: cmds for f, cmds in file_to_commands.items() if len(cmds) > 1}

    print(f"\n发现 {len(conflicts)} 个文件名冲突:")
    for filename, cmds in conflicts.items():
        print(f"\n{filename}.md:")
        for cmd_name, cmd_url in cmds:
            print(f"  - {cmd_name} ({cmd_url})")

    # 检查文件是否存在
    print(f"\n\n文件存在性检查:")
    for filename, cmds in conflicts.items():
        filepath = OUTPUT_DIR / f"{filename}.md"
        if filepath.exists():
            print(f"{filename}.md: 存在 ({filepath.stat().st_size} 字节)")
            # 读取文件第一行查看内容
            with open(filepath, "r", encoding="utf-8") as f:
                first_line = f.readline().strip()
                print(f"  标题: {first_line}")
        else:
            print(f"{filename}.md: 不存在")

    # 统计受影响的命令
    affected_commands = sum(len(cmds) for cmds in conflicts.values())
    print(f"\n受影响的命令总数: {affected_commands}")
    print(f"唯一文件名数量: {len(file_to_commands)}")

    # 生成修复建议
    print(f"\n修复建议:")
    for filename, cmds in conflicts.items():
        if len(cmds) == 2:
            cmd1, cmd2 = cmds[0][0], cmds[1][0]
            print(f"- {filename}.md: {cmd1} 和 {cmd2}")
            print(f"  建议: 为 {cmd1} 创建 {sanitize_filename(cmd1 + '_alt')}.md")
            print(f"        为 {cmd2} 创建 {sanitize_filename(cmd2 + '_alt')}.md")


if __name__ == "__main__":
    main()
