#!/usr/bin/env python3
"""
修复索引文件格式
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.optimize_documentation import (
    Config, CommandMapper, IndexTransformer
)

def main():
    """主函数"""
    print("=" * 60)
    print("修复索引文件格式")
    print("=" * 60)
    
    # 备份当前索引文件
    index_file = Config.INDEX_FILE
    backup_file = index_file.with_suffix(".md.pre_fix_backup")
    if index_file.exists():
        import shutil
        shutil.copy2(index_file, backup_file)
        print(f"已备份当前索引文件: {backup_file}")
    
    # 构建命令映射
    print("\n正在构建命令映射...")
    mapper = CommandMapper()
    if not mapper.build_from_index():
        print("[FAIL] 无法构建命令映射")
        return 1
    
    print(f"成功映射 {len(mapper.commands)} 个命令")
    
    # 创建索引转换器
    transformer = IndexTransformer(mapper)
    
    # 转换并保存索引文件
    print("\n正在转换索引文件格式...")
    if transformer.save_converted_index():
        print("[SUCCESS] 索引文件转换成功")
        
        # 显示新文件的前几行
        print("\n新索引文件前20行:")
        print("-" * 60)
        content = index_file.read_text(encoding="utf-8")
        lines = content.splitlines()[:20]
        for i, line in enumerate(lines, 1):
            print(f"{i:3}: {line}")
        print("-" * 60)
        
        # 检查关键特征
        if "https://optics.ansys.com" in content and "[ANSYS]" in content:
            print("\n✅ 修复成功:")
            print("  - Source行显示原始URL")
            print("  - 官方链接使用'ANSYS'文字")
            print("  - 每个字母部分有独立表格")
        else:
            print("\n⚠️ 警告: 某些特征可能不正确")
            
        return 0
    else:
        print("[FAIL] 索引文件转换失败")
        return 1

if __name__ == "__main__":
    sys.exit(main())