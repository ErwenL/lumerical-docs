#!/usr/bin/env python3
"""自动翻译LSF脚本命令文档 - 保持高质量翻译"""

import re
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
CN_DIR = BASE_DIR / "docs" / "lsf-script" / "cn"
EN_DIR = BASE_DIR / "docs" / "lsf-script" / "en"

# 常见技术术语翻译词典
TECH_TERMS = {
    # 基础术语
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
    'monitor': '监视器',
    'charge monitor': '电荷监视器',
    'presence': '存在',
    'requires': '需要',
    'dimension': '维度',
    'enable': '启用',
    'saving': '保存',
    'file': '文件',
    'filename': '文件名',
    'data': '数据',
    'mat': 'mat',  # 文件扩展名，不翻译
    'enable saving': '启用保存',
    
    # 方向
    'x': 'x',
    'y': 'y',
    'z': 'z',
    'x min': 'x最小值',
    'x max': 'x最大值',
    'y min': 'y最小值',
    'y max': 'y最大值',
    'z min': 'z最小值',
    'z max': 'z最大值',
    'x span': 'x跨度',
    'y span': 'y跨度',
    'z span': 'z跨度',
    
    # 单位
    'microns': '微米',
    'nanometers': '纳米',
    'millimeters': '毫米',
    'meters': '米',
    'seconds': '秒',
    'hertz': '赫兹',
    'wavelength': '波长',
    'frequency': '频率',
    
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

# 句子模式翻译
SENTENCE_PATTERNS = [
    (r'Adds (?:a|an) (.+?) in the simulation space\.', r'在仿真空间中添加\1。'),
    (r'Adds (?:a|an) (.+?) to the (.+?)\.', r'向\2添加\1。'),
    (r'Returns (.+?)\.', r'返回\1。'),
    (r'Creates (.+?)\.', r'创建\1。'),
    (r'Sets (.+?)\.', r'设置\1。'),
    (r'Gets (.+?)\.', r'获取\1。'),
    (r'Calculates (.+?)\.', r'计算\1。'),
    (r'Converts (.+?) to (.+?)\.', r'将\1转换为\2。'),
    (r'This (?:function|command) (?:does not return any data|returns no data)\.', r'此函数不返回任何数据。'),
    (r'This command (.+?)\.', r'此命令\1。'),
    (r'The following script (.+?)\.', r'以下脚本\1。'),
    (r'See example for (.+?) command\.', r'参见\1命令的示例。'),
    (r'To learn more about (.+?) go to this page:', r'要了解更多关于\1的信息，请访问此页面：'),
    (r'(.+?) must be present in (.+?) for this command to work\.', r'\2中必须存在\1，此命令才能工作。'),
    (r'(.+?) can be used to (.+?)\.', r'\1可用于\2。'),
    (r'The (.+?) is set to (.+?)\.', r'\1设置为\2。'),
    (r'The corresponding (.+?) are:', r'对应的\1为：'),
    (r'\.\.\. represents (.+?)', r'... 表示\1'),
]

def translate_text(text: str) -> str:
    """翻译文本，保留代码块和链接"""
    # 分割文本为段落
    lines = text.split('\n')
    translated_lines = []
    
    in_code_block = False
    for line in lines:
        # 检测代码块开始/结束
        if line.strip().startswith('```') or line.strip().startswith('    '):
            in_code_block = not in_code_block
            translated_lines.append(line)
            continue
        
        if in_code_block:
            # 代码块内的内容不翻译
            translated_lines.append(line)
            continue
        
        # 不翻译纯链接行
        if line.strip().startswith('http') or '://' in line:
            translated_lines.append(line)
            continue
        
        # 不翻译HTML注释
        if line.strip().startswith('<!--') or line.strip().startswith('-->'):
            translated_lines.append(line)
            continue
        
        # 保护Markdown链接不被修改
        # 匹配模式: [text](url)
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        
        # 查找所有链接并存储
        links = []
        def store_link(match):
            links.append(match.group(0))
            return f'__LINK_{len(links)-1}__'
        
        # 临时替换链接
        line_without_links = re.sub(link_pattern, store_link, line)
        
        # 应用术语翻译
        translated = line_without_links
        for en, cn in TECH_TERMS.items():
            # 只替换整个单词，避免部分匹配
            translated = re.sub(r'\b' + re.escape(en) + r'\b', cn, translated)
        
        # 应用句子模式
        for pattern, replacement in SENTENCE_PATTERNS:
            translated = re.sub(pattern, replacement, translated, flags=re.IGNORECASE)
        
        # 恢复链接
        for i, link in enumerate(links):
            translated = translated.replace(f'__LINK_{i}__', link)
        
        translated_lines.append(translated)
    
    return '\n'.join(translated_lines)

def translate_file(command_name: str, overwrite: bool = False) -> bool:
    """翻译单个文件"""
    en_file = EN_DIR / f"{command_name}.md"
    cn_file = CN_DIR / f"{command_name}.md"
    
    if not en_file.exists():
        print(f"[错误] 英文文件不存在: {en_file}")
        return False
    
    # 读取英文内容
    en_content = en_file.read_text(encoding='utf-8')
    
    # 读取现有中文内容（如果有）
    cn_content = ""
    if cn_file.exists():
        cn_content = cn_file.read_text(encoding='utf-8')
    
    # 如果中文文件已经有翻译内容且不覆盖，跳过
    if cn_content and "Translation from English documentation" in cn_content and not overwrite:
        print(f"[跳过] 文件已翻译: {command_name}")
        return True
    
    # 生成翻译
    translated = translate_text(en_content)
    
    # 添加翻译头部
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    header = f"""<!--
Translation from English documentation
Original command: {command_name}
Translation date: {timestamp}
-->

"""
    
    # 组合内容
    final_content = header + translated
    
    # 保存
    cn_file.write_text(final_content, encoding='utf-8')
    print(f"[完成] 已翻译: {command_name}")
    return True

def find_files_to_translate() -> list[str]:
    """查找需要翻译的文件"""
    files_to_translate = []
    
    for cn_file in CN_DIR.glob("*.md"):
        try:
            content = cn_file.read_text(encoding='utf-8')
            # 如果文件包含"待翻译文档"标记，需要翻译
            if "待翻译文档" in content:
                files_to_translate.append(cn_file.stem)
        except:
            continue
    
    return files_to_translate

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="自动翻译LSF脚本命令文档")
    parser.add_argument("--command", help="要翻译的命令名称")
    parser.add_argument("--list", action="store_true", help="列出需要翻译的文件")
    parser.add_argument("--batch", type=int, help="批量翻译指定数量的文件")
    parser.add_argument("--overwrite", action="store_true", help="覆盖现有翻译")
    
    args = parser.parse_args()
    
    if args.list:
        files = find_files_to_translate()
        print(f"需要翻译的文件 ({len(files)}个):")
        for i, f in enumerate(files[:50], 1):
            print(f"{i:3d}. {f}")
        if len(files) > 50:
            print(f"... 还有 {len(files) - 50} 个文件")
        return
    
    if args.command:
        success = translate_file(args.command, args.overwrite)
        if not success:
            print("翻译失败")
    elif args.batch:
        files = find_files_to_translate()
        if not files:
            print("没有需要翻译的文件")
            return
        
        count = min(args.batch, len(files))
        print(f"开始批量翻译 {count} 个文件...")
        
        translated = 0
        for i in range(count):
            if translate_file(files[i], args.overwrite):
                translated += 1
        
        print(f"批量翻译完成: {translated}/{count} 个文件")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()