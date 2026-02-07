#!/usr/bin/env python3
"""评估翻译文档质量"""

import re
from pathlib import Path
from typing import Dict, Tuple, List

BASE_DIR = Path(__file__).parent.parent
CN_DIR = BASE_DIR / "docs" / "lsf-script" / "cn"
EN_DIR = BASE_DIR / "docs" / "lsf-script" / "en"

# 技术术语词典
TECH_TERMS = {
    'adds': '添加',
    'Adds': '添加',
    'add': '添加',
    'Add': '添加',
    'returns': '返回',
    'Returns': '返回',
    'return': '返回',
    'Return': '返回',
    'creates': '创建',
    'Creates': '创建',
    'create': '创建',
    'Create': '创建',
    'sets': '设置',
    'Sets': '设置',
    'set': '设置',
    'Set': '设置',
    'gets': '获取',
    'Gets': '获取',
    'get': '获取',
    'Get': '获取',
    'calculates': '计算',
    'Calculates': '计算',
    'calculate': '计算',
    'Calculate': '计算',
    'converts': '转换',
    'Converts': '转换',
    'convert': '转换',
    'Convert': '转换',
    'simulation': '仿真',
    'simulation space': '仿真空间',
    'simulation region': '仿真区域',
    'boundary condition': '边界条件',
    'solver': '求解器',
    'monitor': '监视器',
    'source': '源',
    'port': '端口',
    'material': '材料',
    'property': '属性',
    'properties': '属性',
    'parameter': '参数',
    'parameters': '参数',
    'argument': '参数',
    'arguments': '参数',
    'value': '值',
    'values': '值',
    'function': '函数',
    'command': '命令',
    'script': '脚本',
    'object': '对象',
    'objects': '对象',
    'data': '数据',
    'matrix': '矩阵',
    'vector': '向量',
    'array': '数组',
    'structure': '结构',
    'element': '元素',
    'analysis': '分析',
    'analysis group': '分析组',
    'analysis property': '分析属性',
    'user defined': '用户定义',
    'custom': '自定义',
    'container': '容器',
    'environment': '环境',
    'variable': '变量',
    'type': '类型',
}

def assess_file_quality(cn_file: Path) -> Dict[str, float]:
    """评估单个文件的质量"""
    if not cn_file.exists():
        return {"error": "文件不存在"}
    
    content = cn_file.read_text(encoding='utf-8')
    
    # 基本统计
    total_chars = len(content)
    chinese_chars = sum(1 for char in content if '\u4e00' <= char <= '\u9fff')
    english_chars = sum(1 for char in content if 'a' <= char.lower() <= 'z')
    space_chars = content.count(' ')
    
    # 计算中文覆盖率
    chinese_coverage = chinese_chars / (chinese_chars + english_chars) if (chinese_chars + english_chars) > 0 else 0
    
    # 检查混合翻译模式
    lines = content.split('\n')
    mixed_pattern_score = 0
    mixed_lines = 0
    
    for line in lines:
        # 跳过代码块和链接
        if line.strip().startswith('```') or line.strip().startswith('    ') or '://' in line:
            continue
        
        # 检查是否包含中英文混合
        has_chinese = any('\u4e00' <= char <= '\u9fff' for char in line)
        has_english = any('a' <= char.lower() <= 'z' for char in line)
        
        if has_chinese and has_english:
            # 检查是否是典型的混合翻译模式
            # 例如："添加 an analysis group to the 仿真 environment"
            mixed_terms = [' an ', ' a ', ' the ', ' to ', ' in ', ' of ', ' and ', ' or ', ' with ', ' for ']
            if any(term in line.lower() for term in mixed_terms):
                mixed_lines += 1
    
    mixed_pattern_score = mixed_lines / len(lines) if lines else 0
    
    # 检查术语一致性
    term_consistency = 0
    term_matches = 0
    total_terms = 0
    
    for en_term, cn_term in TECH_TERMS.items():
        # 在内容中查找英文术语
        if en_term.lower() in content.lower():
            total_terms += 1
            # 检查是否已翻译
            if cn_term in content:
                term_matches += 1
    
    term_consistency = term_matches / total_terms if total_terms > 0 else 1.0
    
    # 格式检查
    format_score = 0
    format_checks = 0
    format_passed = 0
    
    # 检查1: 是否有翻译头部
    if "Translation from English documentation" in content:
        format_passed += 1
    format_checks += 1
    
    # 检查2: 是否有正确的标题格式
    if re.search(r'^#\s+\w+', content, re.MULTILINE):
        format_passed += 1
    format_checks += 1
    
    # 检查3: 是否有代码块标记
    if '```' in content or '    ' in content:
        format_passed += 1
    format_checks += 1
    
    format_score = format_passed / format_checks if format_checks > 0 else 0
    
    # 计算总体质量评分
    # 权重: 中文覆盖率 40%，术语一致性 30%，混合模式 20%，格式 10%
    overall_score = (
        chinese_coverage * 0.4 +
        term_consistency * 0.3 +
        (1 - mixed_pattern_score) * 0.2 +  # 混合模式越低越好
        format_score * 0.1
    )
    
    # 确定质量等级
    if overall_score >= 0.8:
        quality_level = "良好"
    elif overall_score >= 0.6:
        quality_level = "中等"
    elif overall_score >= 0.4:
        quality_level = "部分翻译"
    else:
        quality_level = "低质量"
    
    return {
        "filename": cn_file.name,
        "overall_score": round(overall_score, 3),
        "quality_level": quality_level,
        "chinese_coverage": round(chinese_coverage, 3),
        "term_consistency": round(term_consistency, 3),
        "mixed_pattern_score": round(mixed_pattern_score, 3),
        "format_score": round(format_score, 3),
        "total_chars": total_chars,
        "chinese_chars": chinese_chars,
        "english_chars": english_chars,
    }

def assess_batch(file_pattern: str = "*.md", limit: int = 10) -> List[Dict]:
    """评估一批文件"""
    results = []
    files = list(sorted(CN_DIR.glob(file_pattern)))[:limit]
    
    for cn_file in files:
        result = assess_file_quality(cn_file)
        results.append(result)
    
    # 按质量评分排序
    results.sort(key=lambda x: x.get('overall_score', 0))
    
    return results

def print_quality_report(results: List[Dict]):
    """打印质量报告"""
    print("=" * 80)
    print("翻译文档质量评估报告")
    print("=" * 80)
    
    for i, result in enumerate(results, 1):
        print(f"\n{i:3d}. {result['filename']:<30} 评分: {result['overall_score']:.3f} ({result['quality_level']})")
        print(f"    中文覆盖率: {result['chinese_coverage']:.1%} | 术语一致性: {result['term_consistency']:.1%} | "
              f"混合模式: {result['mixed_pattern_score']:.1%} | 格式: {result['format_score']:.1%}")
    
    # 统计摘要
    total = len(results)
    good = sum(1 for r in results if r['quality_level'] == '良好')
    medium = sum(1 for r in results if r['quality_level'] == '中等')
    partial = sum(1 for r in results if r['quality_level'] == '部分翻译')
    low = sum(1 for r in results if r['quality_level'] == '低质量')
    
    print(f"\n{'=' * 80}")
    print("质量分布摘要:")
    print(f"  良好翻译: {good}/{total} ({good/total*100:.1f}%)")
    print(f"  中等质量: {medium}/{total} ({medium/total*100:.1f}%)")
    print(f"  部分翻译: {partial}/{total} ({partial/total*100:.1f}%)")
    print(f"  低质量: {low}/{total} ({low/total*100:.1f}%)")
    
    avg_score = sum(r['overall_score'] for r in results) / total if total > 0 else 0
    print(f"  平均质量评分: {avg_score:.3f}")

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="评估翻译文档质量")
    parser.add_argument("--file", help="评估单个文件")
    parser.add_argument("--batch", type=int, default=20, help="评估一批文件的数量")
    parser.add_argument("--output", help="输出报告文件")
    
    args = parser.parse_args()
    
    if args.file:
        cn_file = CN_DIR / args.file
        if not cn_file.exists():
            cn_file = Path(args.file)
        
        result = assess_file_quality(cn_file)
        print(f"\n文件质量评估: {cn_file.name}")
        print(f"总体评分: {result['overall_score']:.3f} ({result['quality_level']})")
        print(f"中文覆盖率: {result['chinese_coverage']:.1%}")
        print(f"术语一致性: {result['term_consistency']:.1%}")
        print(f"混合模式分数: {result['mixed_pattern_score']:.1%}")
        print(f"格式分数: {result['format_score']:.1%}")
        print(f"字符统计: 总{result['total_chars']} | 中文{result['chinese_chars']} | 英文{result['english_chars']}")
    else:
        results = assess_batch(limit=args.batch)
        print_quality_report(results)
        
        if args.output:
            import json
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f"\n报告已保存到: {args.output}")

if __name__ == "__main__":
    main()