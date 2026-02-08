#!/usr/bin/env python3
"""
测试索引文件转换功能
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.optimize_documentation import (
    Config, CommandMapper, IndexTransformer
)

def test_index_conversion():
    """测试索引文件转换"""
    print("=" * 60)
    print("测试索引文件转换功能")
    print("=" * 60)
    
    # 构建命令映射
    print("正在构建命令映射...")
    mapper = CommandMapper()
    if not mapper.build_from_index():
        print("[FAIL] 无法构建命令映射")
        return False
    
    print(f"成功映射 {len(mapper.commands)} 个命令")
    
    # 创建索引转换器
    transformer = IndexTransformer(mapper)
    
    # 测试转换功能
    print("\n测试索引文件转换...")
    table_content = transformer.convert_to_table()
    
    if not table_content:
        print("[FAIL] 索引转换失败")
        return False
    
    # 检查关键特征
    print("\n检查转换结果:")
    
    # 1. 检查Source行
    if "https://optics.ansys.com" in table_content:
        print("[OK] Source行包含原始URL")
    else:
        print("[FAIL] Source行不包含原始URL")
        
    # 2. 检查表格结构
    lines = table_content.splitlines()
    table_sections = [i for i, line in enumerate(lines) if line.startswith("### ")]
    
    if len(table_sections) > 0:
        print(f"[OK] 找到 {len(table_sections)} 个字母部分")
    else:
        print("[FAIL] 未找到字母部分")
        return False
    
    # 3. 检查每个字母部分是否有完整的表格
    for i, section_idx in enumerate(table_sections):
        section_name = lines[section_idx][4:].strip()
        
        # 检查该部分是否有表头
        has_table_header = False
        for j in range(section_idx + 1, min(section_idx + 5, len(lines))):
            if "| 命令名 | 官方文档 | 本地文档 |" in lines[j]:
                has_table_header = True
                break
        
        if has_table_header:
            print(f"  [OK] {section_name} 部分有完整的表格")
        else:
            print(f"  [FAIL] {section_name} 部分缺少表格表头")
    
    # 4. 检查链接文字
    if "[链接]" in table_content:
        print("[FAIL] 仍然包含中文'链接'文字")
        return False
    elif "[ANSYS]" in table_content:
        print("[OK] 官方链接使用'ANSYS'文字")
    else:
        print("[FAIL] 未找到'ANSYS'链接文字")
        return False
    
    # 5. 检查特殊字符部分
    if "### Misc" in table_content:
        misc_start = table_content.find("### Misc")
        misc_section = table_content[misc_start:misc_start+500]
        if "|" in misc_section and "[" in misc_section:
            print("[OK] Misc部分包含表格和链接")
        else:
            print("[FAIL] Misc部分格式异常")
    
    # 显示示例内容
    print("\n转换后的文件前30行:")
    print("-" * 60)
    for i, line in enumerate(lines[:30]):
        print(f"{i+1:3}: {line}")
    print("-" * 60)
    
    # 保存测试结果
    test_output = Path("test_index_output.md")
    test_output.write_text(table_content, encoding="utf-8")
    print(f"\n测试输出已保存到: {test_output}")
    
    return True

if __name__ == "__main__":
    success = test_index_conversion()
    
    print("\n" + "=" * 60)
    if success:
        print("索引转换测试通过!")
    else:
        print("索引转换测试失败!")
    print("=" * 60)
    
    sys.exit(0 if success else 1)