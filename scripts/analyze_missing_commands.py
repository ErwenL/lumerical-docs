#!/usr/bin/env python3
"""
分析缺失的LSF脚本命令文档。
对比索引文件中的命令和已抓取的文档文件，找出缺失的命令。
"""

import re
import json
from pathlib import Path
from typing import List, Tuple, Set

# 配置文件
INDEX_FILE = (
    Path(__file__).parent.parent / "docs" / "lsf-script-commands-alphabetical.md"
)
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "lsf-script" / "en"
MISSING_FILE = Path(__file__).parent.parent / "docs" / "missing-commands.json"
ANALYSIS_FILE = Path(__file__).parent.parent / "docs" / "lsf-script-analysis.md"


def parse_index_file() -> List[Tuple[str, str]]:
    """解析索引文件，提取所有命令和URL。"""
    commands = []
    pattern = re.compile(r"- \[([^\]]+)\]\(([^)]+)\)")

    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    matches = pattern.findall(content)
    for cmd_name, cmd_url in matches:
        commands.append((cmd_name.strip(), cmd_url.strip()))

    return commands


def get_existing_files() -> Set[str]:
    """获取已存在的Markdown文件名集合（不包含扩展名）。"""
    existing_files = set()
    for md_file in OUTPUT_DIR.glob("*.md"):
        # 去掉扩展名
        existing_files.add(md_file.stem)
    return existing_files


def sanitize_filename(name: str) -> str:
    """将命令名转换为安全的文件名（与抓取脚本使用相同的逻辑）。"""
    original_name = name

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


def analyze_missing_commands():
    """分析缺失的命令并生成报告。"""
    print("=" * 60)
    print("分析缺失的LSF脚本命令")
    print("=" * 60)

    # 解析索引文件
    print("解析索引文件...")
    all_commands = parse_index_file()
    print(f"索引文件中找到 {len(all_commands)} 个命令")

    # 获取已存在的文件
    print("检查已存在的文档文件...")
    existing_files = get_existing_files()
    print(f"找到 {len(existing_files)} 个已存在的文档文件")

    # 找出缺失的命令
    missing_commands = []
    found_commands = []

    for cmd_name, cmd_url in all_commands:
        sanitized_name = sanitize_filename(cmd_name)
        if sanitized_name in existing_files:
            found_commands.append((cmd_name, cmd_url))
        else:
            missing_commands.append((cmd_name, cmd_url))

    print("\n分析结果:")
    print(f"- 总命令数: {len(all_commands)}")
    print(f"- 已抓取文档: {len(found_commands)}")
    print(f"- 缺失命令: {len(missing_commands)}")
    print(f"- 完成率: {len(found_commands) / len(all_commands) * 100:.1f}%")

    # 按字母分组统计缺失命令
    missing_by_letter = {}
    for cmd_name, cmd_url in missing_commands:
        first_char = (
            cmd_name[0].upper() if cmd_name and cmd_name[0].isalpha() else "Misc"
        )
        if first_char not in missing_by_letter:
            missing_by_letter[first_char] = []
        missing_by_letter[first_char].append((cmd_name, cmd_url))

    # 保存缺失命令到JSON文件
    if missing_commands:
        missing_data = {
            "total_missing": len(missing_commands),
            "missing_commands": missing_commands,
            "missing_by_letter": {
                letter: cmds for letter, cmds in missing_by_letter.items()
            },
        }
        with open(MISSING_FILE, "w", encoding="utf-8") as f:
            json.dump(missing_data, f, indent=2, ensure_ascii=False)
        print(f"\n缺失命令列表已保存到: {MISSING_FILE}")

    # 生成分析报告
    generate_analysis_report(
        all_commands, found_commands, missing_commands, missing_by_letter
    )

    return missing_commands


def generate_analysis_report(
    all_commands, found_commands, missing_commands, missing_by_letter
):
    """生成详细的HTML分析报告。"""
    lines = []
    lines.append("# LSF Script 文档抓取分析报告")
    lines.append("")
    lines.append("**生成时间**: 2026-02-01")
    lines.append(f"**索引文件**: `{INDEX_FILE.name}`")
    lines.append(f"**文档目录**: `{OUTPUT_DIR.name}`")
    lines.append("")

    # 总体统计
    lines.append("## 总体统计")
    lines.append("")
    lines.append("| 项目 | 数量 | 比例 |")
    lines.append("|------|------|------|")
    lines.append(f"| 总命令数 | {len(all_commands)} | 100% |")
    lines.append(
        f"| 已抓取文档 | {len(found_commands)} | {len(found_commands) / len(all_commands) * 100:.1f}% |"
    )
    lines.append(
        f"| 缺失命令 | {len(missing_commands)} | {len(missing_commands) / len(all_commands) * 100:.1f}% |"
    )
    lines.append("")

    # 按字母分组统计
    lines.append("## 按字母分组统计")
    lines.append("")
    lines.append("| 字母 | 总命令数 | 已抓取 | 缺失 | 完成率 |")
    lines.append("|------|----------|--------|------|--------|")

    # 统计每个字母的命令
    all_by_letter = {}
    found_by_letter = {}

    for cmd_name, _ in all_commands:
        first_char = (
            cmd_name[0].upper() if cmd_name and cmd_name[0].isalpha() else "Misc"
        )
        all_by_letter[first_char] = all_by_letter.get(first_char, 0) + 1

    for cmd_name, _ in found_commands:
        first_char = (
            cmd_name[0].upper() if cmd_name and cmd_name[0].isalpha() else "Misc"
        )
        found_by_letter[first_char] = found_by_letter.get(first_char, 0) + 1

    # 按字母顺序排序
    sorted_letters = sorted(all_by_letter.keys())

    for letter in sorted_letters:
        total = all_by_letter.get(letter, 0)
        found = found_by_letter.get(letter, 0)
        missing = total - found
        completion_rate = found / total * 100 if total > 0 else 100.0

        status = "✅" if missing == 0 else "⚠️" if completion_rate > 50 else "❌"
        lines.append(
            f"| {letter} | {total} | {found} | {missing} | {completion_rate:.1f}% {status} |"
        )

    # 缺失命令详情
    if missing_commands:
        lines.append("")
        lines.append("## 缺失命令详情")
        lines.append("")

        for letter in sorted(missing_by_letter.keys()):
            cmds = missing_by_letter[letter]
            if cmds:
                lines.append(f"### {letter} ({len(cmds)} 个缺失命令)")
                lines.append("")
                for cmd_name, cmd_url in cmds:
                    lines.append(f"- [{cmd_name}]({cmd_url})")
                lines.append("")

    # 下一步建议
    lines.append("## 下一步建议")
    lines.append("")
    lines.append("1. **重试抓取缺失命令**")
    lines.append("   - 运行重试脚本: `python scripts/retry_missing_commands.py`")
    lines.append("   - 检查网络连接和API限制")
    lines.append("")
    lines.append("2. **验证已抓取文档质量**")
    lines.append("   - 检查文件大小异常（小于1KB的文件）")
    lines.append("   - 验证内容完整性")
    lines.append("")
    lines.append("3. **更新进度跟踪文档**")
    lines.append("   - 更新 `docs/lsf-script-progress.md`")
    lines.append("   - 记录抓取结果和问题")

    # 写入分析报告
    with open(ANALYSIS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"分析报告已保存到: {ANALYSIS_FILE}")


def main():
    """主函数。"""
    try:
        missing_commands = analyze_missing_commands()

        if missing_commands:
            print("\n需要重试的命令:")
            for i, (cmd_name, cmd_url) in enumerate(missing_commands[:20], 1):
                print(f"  {i:3d}. {cmd_name}")
            if len(missing_commands) > 20:
                print(f"  ... 以及 {len(missing_commands) - 20} 个更多命令")

            print(f"\n总共 {len(missing_commands)} 个命令需要重新尝试抓取。")
            print(f"缺失命令列表已保存到: {MISSING_FILE}")
            print(f"分析报告已保存到: {ANALYSIS_FILE}")
        else:
            print("\n✅ 所有命令文档都已成功抓取！")

    except Exception as e:
        print(f"分析过程中出错: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
