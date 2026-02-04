#!/usr/bin/env python3
"""生成翻译进度报告"""

from pathlib import Path
import json
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
CN_DIR = BASE_DIR / "docs" / "lsf-script" / "cn"
EN_DIR = BASE_DIR / "docs" / "lsf-script" / "en"

def generate_report():
    # 统计所有文件
    en_files = set(f.stem for f in EN_DIR.glob("*.md"))
    cn_files = set(f.stem for f in CN_DIR.glob("*.md"))
    
    # 分类
    fully_translated = []  # 已完成翻译（不含"[待翻译]"标记）
    needs_translation = []  # 需要翻译（含"[待翻译]"标记）
    
    for cmd in cn_files:
        cn_file = CN_DIR / f"{cmd}.md"
        content = cn_file.read_text(encoding='utf-8')
        if "[待翻译]" in content:
            needs_translation.append(cmd)
        else:
            fully_translated.append(cmd)
    
    # 生成报告
    report = {
        "generated_at": datetime.now().isoformat(),
        "summary": {
            "total_english": len(en_files),
            "total_chinese": len(cn_files),
            "fully_translated": len(fully_translated),
            "needs_translation": len(needs_translation),
            "completion_rate": round(len(fully_translated) / len(en_files) * 100, 2) if en_files else 0
        },
        "needs_translation_list": sorted(needs_translation),
        "fully_translated_sample": sorted(fully_translated)[:20]
    }
    
    # 保存报告
    report_file = BASE_DIR / "docs" / "translation-report.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    # 打印摘要
    print("=" * 60)
    print("LSF脚本命令文档翻译进度报告")
    print("=" * 60)
    print(f"生成时间: {report['generated_at']}")
    print()
    print("【统计摘要】")
    print(f"  英文文档总数: {report['summary']['total_english']}")
    print(f"  中文文档总数: {report['summary']['total_chinese']}")
    print(f"  已完成翻译: {report['summary']['fully_translated']}")
    print(f"  需要翻译: {report['summary']['needs_translation']}")
    print(f"  完成率: {report['summary']['completion_rate']}%")
    print()
    print("=" * 60)
    
    if needs_translation:
        print(f"\n【需要翻译的命令列表】共 {len(needs_translation)} 个")
        print("-" * 60)
        for i, cmd in enumerate(sorted(needs_translation)[:50], 1):
            print(f"{i:3d}. {cmd}")
        if len(needs_translation) > 50:
            print(f"... 还有 {len(needs_translation) - 50} 个命令")
        print()
    
    print(f"\n详细报告已保存: {report_file}")
    print("=" * 60)
    
    return report

if __name__ == "__main__":
    generate_report()
