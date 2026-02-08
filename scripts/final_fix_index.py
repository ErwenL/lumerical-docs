#!/usr/bin/env python3
"""最终修复索引文件：修复所有路径和表格格式"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
INDEX_FILE = BASE_DIR / "docs" / "lsf-script" / "lsf-script-commands-alphabetical.md"
EN_DIR = BASE_DIR / "docs" / "lsf-script" / "en"


def read_backup_file():
    """读取备份文件以获取原始内容"""
    backup_file = INDEX_FILE.with_suffix('.md.before_path_fix')
    if backup_file.exists():
        return backup_file.read_text(encoding="utf-8")
    else:
        # 如果没有备份，读取当前文件
        return INDEX_FILE.read_text(encoding="utf-8")


def fix_all_links_and_format():
    """修复所有链接和表格格式"""
    print("正在执行最终修复...")
    
    # 读取原始内容
    original_content = read_backup_file()
    
    # 修复所有链接：将 ./command.md 改为 ./en/command.md
    # 修复命令名链接
    fixed_content = re.sub(
        r'\[([^]]+)\]\((\./[^)]+\.md)\)',
        r'[\1](./en/\2)',
        original_content
    )
    
    # 修复本地文档链接（确保不会重复修复）
    # 本地文档链接格式是：[filename.md](./en/filename.md)
    # 我们确保所有链接都正确
    
    # 修复表格格式：每个字母部分应该有完整的表格
    lines = fixed_content.split('\n')
    fixed_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 如果是字母标题 (### A, ### B, etc.)
        if re.match(r'^### [A-Z]$', line.strip()):
            # 添加字母标题
            fixed_lines.append(line)
            
            # 添加一个空行
            fixed_lines.append('')
            
            # 检查下一行是否是表格头，如果不是就添加
            if i + 1 < len(lines) and re.match(r'^\| Command \|', lines[i + 1].strip()):
                # 下一行是表格头，直接添加
                fixed_lines.append(lines[i + 1])
                i += 1
                
                # 添加表格分隔线
                if i + 1 < len(lines) and re.match(r'^\|[-| ]+\|', lines[i + 1].strip()):
                    fixed_lines.append(lines[i + 1])
                    i += 1
                else:
                    # 如果没有分隔线，添加一个标准的分隔线
                    fixed_lines.append('|---------|---------------|------------|')
            else:
                # 添加标准表格头和分隔线
                fixed_lines.append('| Command | Official Docs | Local Docs |')
                fixed_lines.append('|---------|---------------|------------|')
        
        # 如果是重复的表格头，跳过它
        elif re.match(r'^\| Command \|', line.strip()) and i > 0:
            # 检查上一行是否是字母标题后的空行或表格分隔线
            prev_line = lines[i-1].strip() if i > 0 else ""
            if not (re.match(r'^### [A-Z]$', prev_line) or 
                   prev_line == "" or 
                   re.match(r'^\|[-| ]+\|', prev_line)):
                # 这不是字母标题后的第一个表格头，跳过它
                i += 1
                continue
            else:
                fixed_lines.append(line)
        
        # 如果是重复的表格分隔线，跳过它
        elif re.match(r'^\|[-| ]+\|', line.strip()) and i > 0:
            # 检查上一行是否是表格头
            prev_line = lines[i-1].strip() if i > 0 else ""
            if re.match(r'^\| Command \|', prev_line):
                fixed_lines.append(line)
            else:
                # 跳过重复的分隔线
                i += 1
                continue
        
        else:
            fixed_lines.append(line)
        
        i += 1
    
    # 重新组合内容
    final_content = '\n'.join(fixed_lines)
    
    # 清理多余的空行（连续两个以上空行改为一个）
    final_content = re.sub(r'\n\s*\n\s*\n', '\n\n', final_content)
    
    return final_content


def validate_fixes(content):
    """验证修复结果"""
    print("\n验证修复结果:")
    
    # 检查所有链接格式
    print("1. 检查链接格式:")
    
    # 检查命令名链接
    command_links = re.findall(r'\[([^]]+)\]\((\./en/[^)]+\.md)\)', content)
    print(f"   命令名链接数量: {len(command_links)}")
    
    # 检查本地文档链接
    local_doc_links = re.findall(r'\[([^]]+\.md)\]\((\./en/[^)]+\.md)\)', content)
    print(f"   本地文档链接数量: {len(local_doc_links)}")
    
    # 检查路径有效性
    print("\n2. 检查路径有效性:")
    missing_files = []
    for match in re.finditer(r'\[([^]]+\.md)\]\((\./en/([^)]+))\)', content):
        filename = match.group(3)
        file_path = EN_DIR / filename
        if not file_path.exists():
            missing_files.append(filename)
    
    if missing_files:
        print(f"   [WARN] 发现 {len(missing_files)} 个文件不存在:")
        for filename in missing_files[:5]:
            print(f"     - {filename}")
        if len(missing_files) > 5:
            print(f"     ... 还有 {len(missing_files) - 5} 个文件")
    else:
        print("   [OK] 所有文件路径有效")
    
    # 检查表格结构
    print("\n3. 检查表格结构:")
    
    # 统计字母部分
    letter_sections = re.findall(r'^### [A-Z]$', content, re.MULTILINE)
    print(f"   字母部分数量: {len(letter_sections)}")
    
    # 检查表格头数量
    table_headers = re.findall(r'^\| Command \|', content, re.MULTILINE)
    print(f"   表格头数量: {len(table_headers)}")
    
    # 检查是否有重复的表格头
    if len(table_headers) > len(letter_sections):
        print(f"   [WARN] 表格头数量({len(table_headers)})多于字母部分({len(letter_sections)})")
    else:
        print("   [OK] 表格结构正常")
    
    # 检查特殊字符命令
    print("\n4. 检查特殊字符命令:")
    special_chars = re.findall(r'\[([^a-zA-Z0-9]+)\]\(\./en/[^)]+\)', content)
    if special_chars:
        print(f"   特殊字符命令: {len(special_chars)} 个")
        for char in special_chars[:10]:
            print(f"     - {char}")
    
    return len(missing_files) == 0


def write_final_file(content):
    """写入最终文件"""
    # 创建最终备份
    final_backup = INDEX_FILE.with_suffix('.md.final_backup')
    if INDEX_FILE.exists():
        INDEX_FILE.rename(final_backup)
        print(f"已创建最终备份: {final_backup}")
    
    # 写入修复后的文件
    INDEX_FILE.write_text(content, encoding="utf-8")
    print(f"已写入修复后的文件: {INDEX_FILE}")
    
    # 显示文件大小
    file_size = len(content.encode('utf-8'))
    print(f"文件大小: {file_size:,} 字节")


def main():
    print("=" * 60)
    print("索引文件最终修复")
    print("=" * 60)
    
    # 执行修复
    fixed_content = fix_all_links_and_format()
    
    # 验证修复
    is_valid = validate_fixes(fixed_content)
    
    if is_valid:
        print("\n" + "-" * 60)
        print("修复验证通过，准备写入文件...")
        
        # 写入文件
        write_final_file(fixed_content)
        
        # 显示修复后的前几行
        print("\n修复后的文件前30行:")
        print("-" * 40)
        lines = fixed_content.split('\n')
        for i, line in enumerate(lines[:30]):
            print(f"{i+1:3}: {line}")
        print("-" * 40)
        
        print("\n" + "=" * 60)
        print("修复完成！")
        print("=" * 60)
    else:
        print("\n[ERROR] 修复验证失败，请检查问题")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())