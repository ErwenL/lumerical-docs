#!/usr/bin/env python3
"""修复索引文件中的路径问题和表格格式"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
INDEX_FILE = BASE_DIR / "docs" / "lsf-script" / "lsf-script-commands-alphabetical.md"
EN_DIR = BASE_DIR / "docs" / "lsf-script" / "en"


def fix_index_file():
    """修复索引文件中的路径和格式"""
    print("正在修复索引文件路径和格式...")
    
    # 读取原始文件
    content = INDEX_FILE.read_text(encoding="utf-8")
    
    # 修复路径问题：将./command.md 改为 ./en/command.md
    # 但只修复本地文档链接，不修复命令名链接
    fixed_content = content
    
    # 修复本地文档链接
    fixed_content = re.sub(
        r'\| \[(.*?)\]\((\./[^)]+\.md)\) \|',
        lambda m: f'| [{m.group(1)}]({m.group(2)}) |',
        fixed_content
    )
    
    # 修复本地文档列
    fixed_content = re.sub(
        r'\| \[([^]]+\.md)\]\((\./[^)]+\.md)\) \|',
        lambda m: f'| [{m.group(1)}](./en/{m.group(1)}) |',
        fixed_content
    )
    
    # 修复表格格式：确保每个字母部分有完整的表格
    lines = fixed_content.split('\n')
    fixed_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 如果是字母标题
        if line.startswith('### '):
            fixed_lines.append(line)
            i += 1
            
            # 跳过空行
            while i < len(lines) and lines[i].strip() == '':
                i += 1
            
            # 添加表格头
            if i < len(lines) and lines[i].startswith('| Command |'):
                fixed_lines.append(lines[i])
                i += 1
            else:
                # 如果没有表格头，添加一个
                fixed_lines.append('')
                fixed_lines.append('| Command | Official Docs | Local Docs |')
                fixed_lines.append('|---------|---------------|------------|')
        
        else:
            fixed_lines.append(line)
            i += 1
    
    # 重新组合内容
    fixed_content = '\n'.join(fixed_lines)
    
    # 备份原始文件
    backup_file = INDEX_FILE.with_suffix('.md.before_path_fix')
    INDEX_FILE.rename(backup_file)
    print(f"已备份原始文件到: {backup_file}")
    
    # 写入修复后的文件
    INDEX_FILE.write_text(fixed_content, encoding="utf-8")
    print(f"已修复索引文件: {INDEX_FILE}")
    
    # 验证修复结果
    print("\n验证修复结果:")
    
    # 检查路径
    path_errors = []
    for line in fixed_content.split('\n'):
        if './en/' in line:
            # 提取文件名
            match = re.search(r'\[([^]]+\.md)\]\(\./en/([^)]+)\)', line)
            if match:
                filename = match.group(2)
                file_path = EN_DIR / filename
                if not file_path.exists():
                    path_errors.append(f"文件不存在: {filename}")
    
    if path_errors:
        print(f"[WARN] 发现 {len(path_errors)} 个路径问题:")
        for error in path_errors[:10]:  # 只显示前10个
            print(f"  {error}")
        if len(path_errors) > 10:
            print(f"  ... 还有 {len(path_errors) - 10} 个问题")
    else:
        print("[OK] 所有本地文档路径有效")
    
    # 检查表格结构
    table_sections = re.findall(r'### [A-Z]', fixed_content)
    print(f"[OK] 找到 {len(table_sections)} 个字母部分")
    
    # 检查是否有连续的表格头
    double_headers = re.findall(r'\| Command \|.*?\n\| Command \|', fixed_content, re.DOTALL)
    if double_headers:
        print(f"[WARN] 发现 {len(double_headers)} 个重复的表格头")
    else:
        print("[OK] 表格结构正常")


def check_existing_links():
    """检查现有链接"""
    print("\n检查现有链接状态:")
    
    content = INDEX_FILE.read_text(encoding="utf-8")
    
    # 统计链接类型
    local_links = re.findall(r'\[([^]]+\.md)\]\(\./([^)]+)\)', content)
    en_links = re.findall(r'\[([^]]+\.md)\]\(\./en/([^)]+)\)', content)
    ansys_links = re.findall(r'\[ANSYS\]\(https://[^)]+\)', content)
    
    print(f"本地链接 (旧格式): {len(local_links)}")
    print(f"本地链接 (en/格式): {len(en_links)}")
    print(f"ANSYS官方链接: {len(ansys_links)}")
    
    # 检查几个示例文件
    print("\n示例文件检查:")
    test_files = ['abs.md', 'acos.md', 'addfdtd.md']
    for test_file in test_files:
        en_path = EN_DIR / test_file
        if en_path.exists():
            print(f"  [OK] {test_file} 存在于 en/ 目录")
        else:
            print(f"  [FAIL] {test_file} 不存在于 en/ 目录")


if __name__ == "__main__":
    print("=" * 60)
    print("修复索引文件路径和表格格式")
    print("=" * 60)
    
    check_existing_links()
    print("\n" + "-" * 60)
    fix_index_file()