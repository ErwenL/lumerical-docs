#!/usr/bin/env python3
"""检查翻译状态 - 区分真正翻译的文件和模板文件。"""

import sys
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
EN_DOCS_DIR = PROJECT_ROOT / "docs" / "lsf-script" / "en"
CN_DOCS_DIR = PROJECT_ROOT / "docs" / "lsf-script" / "cn"


def check_translation_quality():
    """检查中文文档的翻译质量。"""
    if not CN_DOCS_DIR.exists():
        print("中文文档目录不存在")
        return
    
    cn_files = list(CN_DOCS_DIR.glob("*.md"))
    total_cn = len(cn_files)
    
    categories = {
        "good_translation": [],      # 良好翻译（中文字符多）
        "partial_translation": [],   # 部分翻译
        "bad_translation": [],       # 错误翻译（乱码字符）
        "template_file": [],         # 模板文件
        "english_only": [],          # 基本是英文
    }
    
    problem_files = []  # 有问题的文件
    
    for cn_file in cn_files:
        try:
            with open(cn_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否为模板文件
            if "[待翻译]" in content:
                categories["template_file"].append(cn_file.stem)
                problem_files.append((cn_file.stem, "模板文件"))
                continue
            
            # 分析内容
            lines = content.split('\n')
            chinese_char_count = sum(1 for line in lines for char in line if '\u4e00' <= char <= '\u9fff')
            english_char_count = sum(1 for line in lines for char in line if 'a' <= char.lower() <= 'z')
            total_chars = sum(len(line) for line in lines)
            
            # 检查是否有乱码字符（常见错误翻译字符）
            weird_chars = ['在', '到', '和', '是', '从', '这']  # 这些字符在错误翻译中常见
            weird_count = sum(1 for line in lines for char in line if char in weird_chars)
            
            # 分类
            if total_chars == 0:
                categories["english_only"].append(cn_file.stem)
            elif chinese_char_count > english_char_count * 0.3 and weird_count < chinese_char_count * 0.1:
                categories["good_translation"].append(cn_file.stem)
            elif weird_count > chinese_char_count * 0.5 and weird_count > 5:
                categories["bad_translation"].append(cn_file.stem)
                problem_files.append((cn_file.stem, "错误翻译（乱码）"))
            elif chinese_char_count > 0:
                categories["partial_translation"].append(cn_file.stem)
                problem_files.append((cn_file.stem, "部分翻译"))
            else:
                categories["english_only"].append(cn_file.stem)
                problem_files.append((cn_file.stem, "基本是英文"))
                
        except Exception as e:
            print(f"检查文件失败 {cn_file.name}: {e}")
    
    print("\n" + "=" * 60)
    print("翻译质量详细分析报告")
    print("=" * 60)
    print(f"中文文档总数: {total_cn}")
    print(f"良好翻译: {len(categories['good_translation'])}")
    print(f"部分翻译: {len(categories['partial_translation'])}")
    print(f"错误翻译（乱码）: {len(categories['bad_translation'])}")
    print(f"模板文件: {len(categories['template_file'])}")
    print(f"基本是英文: {len(categories['english_only'])}")
    
    if problem_files:
        print(f"\n需要处理的问题文件（前30个）:")
        for i, (cmd, reason) in enumerate(problem_files[:30], 1):
            print(f"{i:3d}. {cmd} - {reason}")
        if len(problem_files) > 30:
            print(f"... 还有 {len(problem_files) - 30} 个问题文件")
    
    # 检查英文文档数量以确认完整性
    if EN_DOCS_DIR.exists():
        en_files = list(EN_DOCS_DIR.glob("*.md"))
        total_en = len(en_files)
        print(f"\n英文文档总数: {total_en}")
        print(f"覆盖率: {total_cn}/{total_en} = {total_cn/total_en*100:.1f}%")
    
    return problem_files


if __name__ == "__main__":
    check_translation_quality()