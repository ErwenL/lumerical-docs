#!/usr/bin/env python3
"""
批量翻译 LSF 脚本命令文档
找出所有需要翻译的文件并进行翻译
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

# 目录路径
CN_DIR = Path("docs/lsf-script/cn")
EN_DIR = Path("docs/lsf-script/en")

# 优先翻译的文件模式
PRIORITY_PATTERNS = [
    # 数学函数
    r'^(acos|asin|atan|atan2|cos|sin|tan|cosh|sinh|tanh|exp|log|log10|sqrt|abs|ceil|floor|round|mod|pow|sign|sinhc|sinc|tanhc)$',
    # 文件操作
    r'^(write|read|save|load|import|export|print|fileexists)$',
    # 数据操作
    r'^(reshape|transpose|integrate|interpolate|find|length|size|pinch|squeeze|sum|mean|max|min|abs)$',
    # 仿真相关
    r'^(grating|fft|farfield|nearfield|overlap|power|transmission|reflection|sourcepower)$',
]

def find_files_needing_translation() -> List[Tuple[Path, Path, int]]:
    """
    找出所有需要翻译的文件
    返回: [(cn_file, en_file, priority_score), ...]
    """
    files_to_translate = []
    
    for cn_file in CN_DIR.glob("*.md"):
        en_file = EN_DIR / cn_file.name
        if not en_file.exists():
            continue
            
        content = cn_file.read_text(encoding='utf-8')
        
        # 检查是否包含"[待翻译]"标记或明显的模板内容
        needs_translation = False
        
        if "[待翻译]" in content:
            needs_translation = True
        
        # 检查是否只有元数据但没有实质内容
        lines = content.split('\n')
        content_lines = [l for l in lines if l.strip() and not l.startswith(('---', 'command:', 'category:', 'description:', 'updated:'))]
        if len(content_lines) < 5:  # 内容太少，可能是模板
            needs_translation = True
        
        # 检查是否包含大量英文（可能是未翻译）
        english_words = re.findall(r'\b[A-Za-z]{4,}\b', content)
        if len(english_words) > 20:  # 如果有很多英文单词，可能需要翻译
            needs_translation = True
        
        if needs_translation:
            # 计算优先级分数
            priority = 0
            command_name = cn_file.stem
            
            for pattern in PRIORITY_PATTERNS:
                if re.match(pattern, command_name, re.IGNORECASE):
                    priority = 100
                    break
            
            files_to_translate.append((cn_file, en_file, priority))
    
    # 按优先级排序
    files_to_translate.sort(key=lambda x: x[2], reverse=True)
    return files_to_translate

if __name__ == "__main__":
    files = find_files_needing_translation()
    print(f"找到 {len(files)} 个需要翻译的文件")
    
    # 显示前20个
    for i, (cn, en, priority) in enumerate(files[:20]):
        print(f"{i+1}. {cn.name} (优先级: {priority})")
