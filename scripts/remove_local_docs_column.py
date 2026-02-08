#!/usr/bin/env python3
"""移除索引文件中的Local Docs列"""

import re
from pathlib import Path
from typing import Optional

def remove_local_docs_column(input_file: Path, output_file: Optional[Path] = None):
    """从索引文件中移除Local Docs列"""
    if output_file is None:
        output_file = input_file
    
    content = input_file.read_text(encoding="utf-8")
    lines = content.splitlines()
    result_lines = []
    
    for line in lines:
        # 处理表头行
        if "Command | Official Docs | Local Docs" in line:
            # 移除Local Docs列
            line = line.replace(" | Local Docs", "")
            result_lines.append(line)
            continue
        
        # 处理表格分隔行
        if line.startswith("|--") and line.endswith("|"):
            # 移除第三列的分隔符
            # 原始格式: |---|---|---|
            # 新格式: |---|---|
            parts = line.split("|")
            # 移除空字符串（开头和结尾的分割会产生空字符串）
            parts = [p for p in parts if p != ""]
            if len(parts) >= 3:
                # 移除最后一列
                parts = parts[:2]
                # 重建行: |---|---|
                line = "|" + "|".join(parts) + "|"
            result_lines.append(line)
            continue
        
        # 处理数据行（表格行）
        # 匹配格式: | [command](./en/...) | [ANSYS](url) | [file.md](./en/...) |
        if line.startswith("|") and "./en/" in line and not line.startswith("|---"):
            # 按管道符分割，注意处理空值
            parts = line.split("|")
            # 移除第一个和最后一个空字符串（因为行以|开头和|结尾）
            if len(parts) >= 5:  # 应该有5部分: "", " col1 ", " col2 ", " col3 ", ""
                # 保留前两列内容（包含原始空格）
                col1 = parts[1]  # 保持原始空格
                col2 = parts[2]  # 保持原始空格
                # 重建为两列表格行，保留原始格式
                line = f"|{col1}|{col2}|"
            result_lines.append(line)
            continue
        
        # 其他行保持不变
        result_lines.append(line)
    
    # 写入输出文件
    output_file.write_text("\n".join(result_lines), encoding="utf-8")
    print(f"已处理: {input_file.name}")
    print(f"输出: {output_file.name}")

if __name__ == "__main__":
    import sys
    
    index_file = Path(__file__).parent.parent / "docs" / "lsf-script" / "lsf-script-commands-alphabetical.md"
    
    if len(sys.argv) > 1:
        output_file = Path(sys.argv[1])
    else:
        output_file = None
    
    remove_local_docs_column(index_file, output_file)