#!/usr/bin/env python3
"""从原始文件创建正确的索引文件"""

import re
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).parent.parent
ORIGINAL_FILE = BASE_DIR / "docs" / "lsf-script" / "lsf-script-commands-alphabetical.md.original"
INDEX_FILE = BASE_DIR / "docs" / "lsf-script" / "lsf-script-commands-alphabetical.md"
EN_DIR = BASE_DIR / "docs" / "lsf-script" / "en"


def parse_original_file():
    """解析原始文件，提取命令和URL"""
    print("正在解析原始文件...")
    
    content = ORIGINAL_FILE.read_text(encoding="utf-8")
    
    # 按字母分组
    commands_by_letter = defaultdict(list)
    current_letter = None
    
    for line in content.split('\n'):
        line = line.strip()
        
        # 检查是否是字母标题
        if line.startswith('## '):
            current_letter = line[3:].strip()  # 提取字母
            if current_letter == 'Misc':
                current_letter = 'Misc'
            elif len(current_letter) == 1:
                current_letter = current_letter.upper()
            else:
                current_letter = None
                
        # 检查是否是命令项
        elif line.startswith('- ['):
            match = re.match(r'- \[([^]]+)\]\((https://[^)]+)\)', line)
            if match:
                command_name = match.group(1)
                url = match.group(2)
                
                if current_letter:
                    commands_by_letter[current_letter].append((command_name, url))
    
    # 统计
    total_commands = sum(len(cmds) for cmds in commands_by_letter.values())
    print(f"解析完成: {len(commands_by_letter)} 个字母组, {total_commands} 个命令")
    
    return commands_by_letter


def get_filename_for_command(command_name):
    """获取命令对应的文件名"""
    # 特殊字符映射
    special_chars = {
        '!': 'exclamation',
        '!=': 'exclamationequals',
        '"': 'quote',
        '#': 'hash',
        '%': 'percent',
        '&': 'ampersand',
        "'": 'apostrophe',
        '*': 'asterisk',
        '+': 'plus',
        '-': 'minus',
        '.': 'dot',
        '/': 'slash',
        ':': 'colon',
        '<': 'lt',
        '<=': 'lte',
        '=': 'equals',
        '==': 'equalsequals',
        '>': 'gt',
        '>=': 'gte',
        '?': 'question',
        '@': 'at',
        '[': 'lbracket',
        ']': 'rbracket',
        '^': 'caret',
        '_': 'underscore',
        '`': 'backtick',
        '{': 'lbrace',
        '|': 'pipe',
        '}': 'rbrace',
        '~': 'tilde',
        '[]': 'lbracketrbracket',
    }
    
    # 检查是否是特殊字符
    if command_name in special_chars:
        return f"{special_chars[command_name]}.md"
    
    # 普通命令：直接使用命令名 + .md
    return f"{command_name}.md"


def create_table_section(letter, commands):
    """创建字母部分的表格"""
    section_lines = []
    
    # 字母标题
    section_lines.append(f"### {letter}")
    section_lines.append("")
    
    # 表格头
    section_lines.append("| Command | Official Docs | Local Docs |")
    section_lines.append("|---------|---------------|------------|")
    
    # 表格行
    for command_name, url in commands:
        filename = get_filename_for_command(command_name)
        
        # 构建行
        # 命令名链接到 ./en/filename.md
        # 官方链接使用 [ANSYS](url)
        # 本地文档链接使用 [filename.md](./en/filename.md)
        row = f"| [{command_name}](./en/{filename}) | [ANSYS]({url}) | [{filename}](./en/{filename}) |"
        section_lines.append(row)
    
    section_lines.append("")  # 空行分隔
    
    return section_lines


def verify_files_exist(commands_by_letter):
    """验证所有文件都存在"""
    print("\n验证文件存在性...")
    
    missing_files = []
    
    for letter, commands in commands_by_letter.items():
        for command_name, url in commands:
            filename = get_filename_for_command(command_name)
            file_path = EN_DIR / filename
            
            if not file_path.exists():
                missing_files.append((command_name, filename))
    
    if missing_files:
        print(f"[WARN] 发现 {len(missing_files)} 个缺失文件:")
        for command_name, filename in missing_files[:10]:
            print(f"  - {command_name} -> {filename}")
        if len(missing_files) > 10:
            print(f"  ... 还有 {len(missing_files) - 10} 个")
    else:
        print("[OK] 所有文件都存在")
    
    return len(missing_files) == 0


def create_index_file(commands_by_letter):
    """创建索引文件"""
    print("\n创建索引文件...")
    
    # 文件头部
    lines = [
        "# Lumerical Script Commands (Alphabetical)",
        "",
        "Source: https://optics.ansys.com/hc/en-us/articles/360034923553-Lumerical-scripting-language-Alphabetical-list",
        "",
    ]
    
    # 按字母顺序处理
    sorted_letters = sorted(commands_by_letter.keys())
    
    for letter in sorted_letters:
        commands = commands_by_letter[letter]
        if commands:  # 只处理有命令的字母
            section_lines = create_table_section(letter, commands)
            lines.extend(section_lines)
    
    # 写入文件
    content = '\n'.join(lines)
    
    # 备份当前文件
    if INDEX_FILE.exists():
        backup_file = INDEX_FILE.with_suffix('.md.backup_before_recreate')
        INDEX_FILE.rename(backup_file)
        print(f"已备份当前文件到: {backup_file}")
    
    # 写入新文件
    INDEX_FILE.write_text(content, encoding="utf-8")
    print(f"已创建新索引文件: {INDEX_FILE}")
    print(f"文件大小: {len(content):,} 字节")
    
    return content


def main():
    print("=" * 60)
    print("从原始文件创建正确的索引文件")
    print("=" * 60)
    
    # 解析原始文件
    commands_by_letter = parse_original_file()
    
    # 验证文件存在性
    all_files_exist = verify_files_exist(commands_by_letter)
    
    if not all_files_exist:
        print("\n[WARN] 有些文件缺失，但继续创建索引文件...")
    
    # 创建索引文件
    content = create_index_file(commands_by_letter)
    
    # 显示前几行
    print("\n创建的文件前30行:")
    print("-" * 40)
    for i, line in enumerate(content.split('\n')[:30]):
        print(f"{i+1:3}: {line}")
    print("-" * 40)
    
    # 统计信息
    print("\n统计信息:")
    total_commands = sum(len(cmds) for cmds in commands_by_letter.values())
    print(f"字母组数量: {len(commands_by_letter)}")
    print(f"命令总数: {total_commands}")
    
    # 按字母统计
    print("\n按字母统计:")
    for letter in sorted(commands_by_letter.keys()):
        count = len(commands_by_letter[letter])
        if count > 0:
            print(f"  {letter}: {count:3} 个命令")
    
    print("\n" + "=" * 60)
    print("创建完成！")
    print("=" * 60)
    
    return 0


if __name__ == "__main__":
    exit(main())