#!/usr/bin/env python3
"""改进部分翻译文档的质量"""

import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

BASE_DIR = Path(__file__).parent.parent
CN_DIR = BASE_DIR / "docs" / "lsf-script" / "cn"
EN_DIR = BASE_DIR / "docs" / "lsf-script" / "en"

# 扩展的技术术语词典
TECH_TERMS = {
    # 基础动词
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
    'deletes': '删除',
    'Deletes': '删除',
    'delete': '删除',
    'Delete': '删除',
    'removes': '移除',
    'Removes': '移除',
    'remove': '移除',
    'Remove': '移除',
    'clears': '清除',
    'Clears': '清除',
    'clear': '清除',
    'Clear': '清除',
    
    # 文档结构
    'Syntax': '语法',
    'Description': '描述',
    'Example': '示例',
    'Examples': '示例',
    'See Also': '参见',
    'Note': '注意',
    'Notes': '注意',
    'Warning': '警告',
    'Important': '重要',
    
    # 技术概念
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
    'length': '长度',
    'time': '时间',
    'frequency': '频率',
    'cell': '单元格',
    'struct': '结构体',
    'number': '数字',
    'string': '字符串',
    'selected': '选中的',
    'corresponding': '对应的',
    'new': '新的',
    'user': '用户',
    'charge': '电荷',
    'presence': '存在',
    'requires': '需要',
    'dimension': '维度',
    'enable': '启用',
    'saving': '保存',
    'file': '文件',
    'filename': '文件名',
    
    # 冠词和连接词
    'a': '一个',
    'an': '一个',
    'the': '该',
    'to': '到',
    'in': '在',
    'on': '在',
    'with': '使用',
    'for': '用于',
    'of': '的',
    'and': '和',
    'or': '或',
    'is': '是',
    'are': '是',
    'be': '为',
    'by': '通过',
    'using': '使用',
    'from': '从',
    'this': '此',
    'that': '该',
    'these': '这些',
    'those': '那些',
    'which': '该',
    'can': '可以',
    'must': '必须',
    'should': '应该',
    'will': '将',
    'may': '可能',
    'if': '如果',
    'then': '那么',
    'else': '否则',
    'when': '当',
    'where': '其中',
    'how': '如何',
    'why': '为什么',
    'what': '什么',
    'who': '谁',
}

# 句子模式转换规则
SENTENCE_PATTERNS = [
    # 模式: Adds X to Y
    (r'Adds (?:a|an) (.+?) (?:to|in) (?:the )?(.+)\.', r'向\2添加\1。'),
    (r'添加 (?:a|an) (.+?) (?:to|in) (?:the )?(.+)\.', r'向\2添加\1。'),
    
    # 模式: Returns X
    (r'Returns (.+?)\.', r'返回\1。'),
    (r'返回 (.+?)\.', r'返回\1。'),
    
    # 模式: Creates X
    (r'Creates (.+?)\.', r'创建\1。'),
    (r'创建 (.+?)\.', r'创建\1。'),
    
    # 模式: This function does not return any data
    (r'This (?:function|command) (?:does not return any data|returns no data)\.', r'此函数不返回任何数据。'),
    
    # 模式: The following script
    (r'The following script (.+?)\.', r'以下脚本\1。'),
    
    # 模式: See example for X command
    (r'See example for (.+?) command\.', r'参见\1命令的示例。'),
    
    # 模式: X must be present in Y for this command to work
    (r'(.+?) must be present in (.+?) for this command to work\.', r'\2中必须存在\1，此命令才能工作。'),
    
    # 模式: X can be used to Y
    (r'(.+?) can be used to (.+?)\.', r'\1可用于\2。'),
    
    # 混合模式修复
    (r'添加 an (.+?) to the (.+?)\.', r'向\2添加\1。'),
    (r'添加 a (.+?) to the (.+?)\.', r'向\2添加\1。'),
    (r'This 函数 does not 返回 any 数据\.', r'此函数不返回任何数据。'),
    (r'在 仿真 空间中 添加 an (.+?)\.', r'在仿真空间中添加\1。'),
]

def improve_sentence(sentence: str) -> str:
    """改进单个句子的翻译质量，保护链接内容"""
    # 首先，保护Markdown链接不被修改
    # 匹配模式: [text](url)
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    # 查找所有链接并存储
    links = []
    def store_link(match):
        links.append(match.group(0))
        return f'__LINK_{len(links)-1}__'
    
    # 临时替换链接
    text_without_links = re.sub(link_pattern, store_link, sentence)
    
    # 应用术语翻译
    improved = text_without_links
    for en, cn in TECH_TERMS.items():
        # 只替换整个单词，避免部分匹配
        improved = re.sub(r'\b' + re.escape(en) + r'\b', cn, improved)
    
    # 应用句子模式
    for pattern, replacement in SENTENCE_PATTERNS:
        improved = re.sub(pattern, replacement, improved, flags=re.IGNORECASE)
    
    # 修复常见的混合模式问题
    # 1. 移除多余的空格
    improved = re.sub(r'\s+', ' ', improved)
    
    # 2. 修复"的的"重复
    improved = re.sub(r'的的', '的', improved)
    
    # 3. 修复"一个一个"重复
    improved = re.sub(r'一个一个', '一个', improved)
    
    # 4. 智能标点替换 - 只替换作为句子结束的标点
    # 先替换逗号
    improved = re.sub(r'([^0-9]),', r'\1，', improved)
    # 再替换句点 - 只替换不在数字中和不在URL中的句点
    # 匹配不在数字中间且后面是空格或行尾的句点
    improved = re.sub(r'(?<!\d)\.(?=\s|$)', '。', improved)
    # 处理缩写和文件扩展名 - 保留它们
    improved = re.sub(r'(\w)\.(\w)', r'\1.\2', improved)
    
    # 恢复链接
    for i, link in enumerate(links):
        improved = improved.replace(f'__LINK_{i}__', link)
    
    return improved.strip()

def improve_content(content: str) -> str:
    """改进整个文档内容"""
    lines = content.split('\n')
    improved_lines = []
    
    in_code_block = False
    for line in lines:
        # 检测代码块开始/结束
        if line.strip().startswith('```') or (line.startswith('    ') and len(line.strip()) > 0):
            in_code_block = not in_code_block
            improved_lines.append(line)
            continue
        
        if in_code_block:
            # 代码块内的内容不改进
            improved_lines.append(line)
            continue
        
        # 不翻译纯链接行
        if line.strip().startswith('http') or '://' in line:
            improved_lines.append(line)
            continue
        
        # 不翻译HTML注释
        if line.strip().startswith('<!--') or line.strip().startswith('-->'):
            improved_lines.append(line)
            continue
        
        # 改进句子
        improved_line = improve_sentence(line)
        improved_lines.append(improved_line)
    
    return '\n'.join(improved_lines)

def improve_file(command_name: str, backup: bool = True) -> Dict:
    """改进单个文件"""
    cn_file = CN_DIR / f"{command_name}.md"
    en_file = EN_DIR / f"{command_name}.md"
    
    if not cn_file.exists():
        return {"success": False, "error": f"中文文件不存在: {cn_file}"}
    
    # 读取现有内容
    cn_content = cn_file.read_text(encoding='utf-8')
    
    # 备份原始文件
    backup_file = None
    if backup:
        backup_file = CN_DIR / f"{command_name}.backup_quality.md"
        backup_file.write_text(cn_content, encoding='utf-8')
    
    # 改进内容
    improved_content = improve_content(cn_content)
    
    # 更新翻译时间
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    improved_content = re.sub(
        r'Translation date: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',
        f'Translation date: {timestamp}',
        improved_content
    )
    
    # 保存改进后的文件
    cn_file.write_text(improved_content, encoding='utf-8')
    
    # 计算改进统计
    original_chinese = sum(1 for char in cn_content if '\u4e00' <= char <= '\u9fff')
    improved_chinese = sum(1 for char in improved_content if '\u4e00' <= char <= '\u9fff')
    improvement_rate = (improved_chinese - original_chinese) / len(cn_content) * 100 if len(cn_content) > 0 else 0
    
    return {
        "success": True,
        "filename": command_name,
        "original_chinese_chars": original_chinese,
        "improved_chinese_chars": improved_chinese,
        "improvement_rate": round(improvement_rate, 2),
        "backup_file": backup_file.name if backup_file else None,
    }

def find_files_needing_improvement(limit: int = 20) -> List[str]:
    """查找需要质量改进的文件"""
    files_needing_improvement = []
    
    for cn_file in CN_DIR.glob("*.md"):
        # 跳过备份文件
        if 'backup' in cn_file.name:
            continue
        
        content = cn_file.read_text(encoding='utf-8', errors='ignore')
        
        # 检查是否是部分翻译（包含混合模式）
        # 混合模式特征：包含英文冠词和中文的混合
        mixed_patterns = [
            ' an ', ' a ', ' the ',  # 英文冠词
            ' to ', ' in ', ' of ', ' and ', ' or ',  # 英文连接词
            ' is ', ' are ', ' be ', ' was ', ' were ',  # 英文系动词
        ]
        
        has_mixed = any(pattern in content.lower() for pattern in mixed_patterns)
        has_chinese = any('\u4e00' <= char <= '\u9fff' for char in content)
        has_english = any('a' <= char.lower() <= 'z' for char in content)
        
        # 如果是混合翻译且包含中文和英文，需要改进
        if has_mixed and has_chinese and has_english:
            files_needing_improvement.append(cn_file.stem)
        
        if len(files_needing_improvement) >= limit:
            break
    
    return files_needing_improvement

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="改进翻译文档质量")
    parser.add_argument("--command", help="要改进的命令名称")
    parser.add_argument("--list", action="store_true", help="列出需要改进的文件")
    parser.add_argument("--batch", type=int, help="批量改进指定数量的文件")
    parser.add_argument("--no-backup", action="store_true", help="不创建备份文件")
    parser.add_argument("--limit", type=int, default=20, help="列出文件时的数量限制")
    
    args = parser.parse_args()
    
    if args.list:
        files = find_files_needing_improvement(limit=args.limit)
        print(f"需要质量改进的文件 ({len(files)}个):")
        for i, f in enumerate(files[:50], 1):
            print(f"{i:3d}. {f}")
        if len(files) > 50:
            print(f"... 还有 {len(files) - 50} 个文件")
        return
    
    if args.command:
        result = improve_file(args.command, not args.no_backup)
        if result["success"]:
            print(f"[成功] 已改进: {result['filename']}")
            print(f"  中文字符数: {result['original_chinese_chars']} → {result['improved_chinese_chars']}")
            print(f"  改进率: {result['improvement_rate']}%")
            if result["backup_file"]:
                print(f"  备份文件: {result['backup_file']}")
        else:
            print(f"[失败] {result['error']}")
    
    elif args.batch:
        files = find_files_needing_improvement(limit=args.batch * 2)  # 获取更多文件以防有些不需要改进
        files = files[:args.batch]  # 只取需要的数量
        
        if not files:
            print("没有找到需要改进的文件")
            return
        
        print(f"开始批量改进 {len(files)} 个文件...")
        
        successful = 0
        for i, cmd in enumerate(files, 1):
            result = improve_file(cmd, not args.no_backup)
            if result["success"]:
                successful += 1
                print(f"{i:3d}. [+] {cmd} (改进率: {result['improvement_rate']}%)")
            else:
                print(f"{i:3d}. [-] {cmd} ({result.get('error', '未知错误')})")
        
        print(f"\n批量改进完成: {successful}/{len(files)} 个文件成功")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()