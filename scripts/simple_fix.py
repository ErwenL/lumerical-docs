#!/usr/bin/env python3
"""简单修复索引文件：只修复命令名链接路径"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
INDEX_FILE = BASE_DIR / "docs" / "lsf-script" / "lsf-script-commands-alphabetical.md"

def fix_command_links():
    """只修复命令名链接，不改变其他格式"""
    print("正在修复命令名链接路径...")
    
    # 读取当前文件
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 备份当前文件
    backup_file = INDEX_FILE.with_suffix('.md.before_simple_fix')
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"已备份到: {backup_file}")
    
    # 修复命令名链接：将 [command](./command.md) 改为 [command](./en/command.md)
    # 但只修复命令名链接，不修复本地文档链接
    # 命令名链接模式：| [command](./command.md) | [ANSYS](... | [command.md](./en/command.md) |
    
    # 更精确的匹配：匹配表格行中的第一个链接
    def replace_command_link(match):
        # match.group(1) 是整个匹配的行
        line = match.group(1)
        # 替换第一个 ./command.md 为 ./en/command.md
        line = re.sub(r'(\[([^]]+)\]\(\./)([^)]+\.md)(\))', r'\1en/\3\4', line, count=1)
        return line
    
    # 匹配表格行
    fixed_content = re.sub(
        r'(\| \[([^]]+)\]\(\./[^)]+\.md\) \| \[ANSYS\]\([^)]+\) \| \[([^]]+\.md)\]\(\./en/[^)]+\.md\) \|)',
        replace_command_link,
        content
    )
    
    # 如果上面的正则没有匹配所有，使用更通用的方法
    # 直接替换所有 | [command](./command.md) 模式
    lines = fixed_content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # 检查是否是表格行
        if line.strip().startswith('|') and '| [ANSYS](' in line:
            # 修复命令名链接
            line = re.sub(r'(\[([^]]+)\]\(\./)([^)]+\.md)(\))', r'\1en/\3\4', line, count=1)
        fixed_lines.append(line)
    
    fixed_content = '\n'.join(fixed_lines)
    
    # 写入修复后的文件
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"已修复文件: {INDEX_FILE}")
    
    # 验证修复
    print("\n验证修复结果:")
    
    # 统计修复的链接
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        new_content = f.read()
    
    # 检查命令名链接
    command_links = re.findall(r'\| \[([^]]+)\]\(\./en/[^)]+\.md\) \|', new_content)
    print(f"已修复的命令名链接: {len(command_links)} 个")
    
    # 检查本地文档链接
    local_links = re.findall(r'\| \[([^]]+\.md)\]\(\./en/[^)]+\.md\) \|', new_content)
    print(f"本地文档链接: {len(local_links)} 个")
    
    # 检查示例
    print("\n示例行:")
    for line in new_content.split('\n')[:5]:
        if '| [abs](' in line:
            print(f"  {line}")
            break
    
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("简单修复：只修复命令名链接路径")
    print("=" * 60)
    
    fix_command_links()
    
    print("\n" + "=" * 60)
    print("修复完成！")
    print("=" * 60)