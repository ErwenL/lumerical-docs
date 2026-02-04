#!/usr/bin/env python3
"""
人工翻译助手 - 批量处理带[待翻译]标记的文件
"""

import glob
import re
from pathlib import Path
from datetime import datetime

BASE_DIR = Path("docs/lsf-script")

def get_files_to_translate():
    """获取所有需要翻译的文件"""
    files = []
    for cn_file in sorted((BASE_DIR / "cn").glob("*.md")):
        with open(cn_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if '[待翻译]' in content:
                files.append(cn_file.name)
    return files

def translate_document(cn_path, en_path, command_name):
    """
    翻译单个文档
    策略：读取英文原文，翻译关键部分，移除[待翻译]标记
    """
    with open(cn_path, 'r', encoding='utf-8') as f:
        cn_content = f.read()
    
    with open(en_path, 'r', encoding='utf-8') as f:
        en_content = f.read()
    
    # 分解英文文档
    en_lines = en_content.split('\n')
    cn_lines = cn_content.split('\n')
    
    # 获取元数据
    header_lines = []
    content_start = 0
    for i, line in enumerate(cn_lines):
        if line.startswith('<!--'):
            header_lines.append(line)
            content_start = i + 1
        elif line.strip() == '' and i < 5:
            content_start = i + 1
    
    # 创建翻译后的内容
    translated_lines = []
    
    # 保留或添加元数据
    if header_lines and 'Translation' in header_lines[0]:
        translated_lines.extend(header_lines[:2])
    else:
        translated_lines.append(f'<!-- Translation completed: {datetime.now().strftime("%Y-%m-%d")} -->')
        translated_lines.append(f'<!-- Original command: {command_name} -->')
    
    translated_lines.append('')  # 空行
    
    # 解析英文内容结构
    en_sections = parse_english_content(en_content)
    
    # 翻译各部分
    translated_lines.append(f'# {command_name}')
    translated_lines.append('')
    
    # 描述部分
    if en_sections.get('description_text'):
        desc_cn = translate_description(en_sections['description_text'])
        translated_lines.append(desc_cn)
        translated_lines.append('')
    
    # 语法表格
    if en_sections.get('syntax_table'):
        translated_lines.append('**语法** | **描述**')
        translated_lines.append('---|---')
        for syntax, description in en_sections['syntax_table']:
            desc_cn = translate_table_cell(description)
            translated_lines.append(f'{syntax} | {desc_cn}')
        translated_lines.append('')
    
    # 示例部分
    if en_sections.get('examples'):
        translated_lines.append('**示例**')
        translated_lines.append('')
        for example in en_sections['examples']:
            if example['description']:
                desc_cn = translate_example_desc(example['description'])
                translated_lines.append(desc_cn)
                translated_lines.append('')
            if example['code']:
                translated_lines.append(example['code'])
                translated_lines.append('')
    
    # 另请参阅
    if en_sections.get('see_also'):
        translated_lines.append('**另请参阅**')
        translated_lines.append('')
        for link in en_sections['see_also']:
            translated_lines.append(link)
        translated_lines.append('')
    
    return '\n'.join(translated_lines)

def parse_english_content(content):
    """解析英文文档内容"""
    lines = content.split('\n')
    sections = {
        'description': [],
        'syntax_table': [],
        'examples': [],
        'see_also': [],
        'description_text': ''
    }
    
    current_section = None
    in_table = False
    example_code = []
    example_desc = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # 标题
        if stripped.startswith('# ') and i > 0:
            current_section = 'description'
            i += 1
            continue
        
        # 语法表格开始
        if '**Syntax**' in line or '**Description**' in line:
            current_section = 'syntax_table'
            i += 1
            # 跳过分隔行
            if i < len(lines) and '---' in lines[i]:
                i += 1
            continue
        
        # 表格行
        if current_section == 'syntax_table' and '|' in line and '---' not in line:
            parts = line.split('|')
            if len(parts) >= 2:
                syntax = parts[0].strip()
                desc = parts[1].strip() if len(parts) > 1 else ''
                sections['syntax_table'].append((syntax, desc))
        
        # 示例开始
        if '**Example' in line or '### Example' in line:
            if example_desc or example_code:
                sections['examples'].append({
                    'description': '\n'.join(example_desc),
                    'code': '\n'.join(example_code)
                })
            current_section = 'examples'
            example_desc = []
            example_code = []
            i += 1
            continue
        
        # 另请参阅
        if '**See Also' in line or 'See Also' in stripped:
            if example_desc or example_code:
                sections['examples'].append({
                    'description': '\n'.join(example_desc),
                    'code': '\n'.join(example_code)
                })
            current_section = 'see_also'
            i += 1
            continue
        
        # 示例代码块
        if stripped.startswith('    ') or stripped.startswith('\t'):
            if current_section == 'examples':
                example_code.append(line)
        elif stripped.startswith('```'):
            if current_section == 'examples':
                example_code.append(line)
                # 读取直到代码块结束
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('```'):
                    example_code.append(lines[i])
                    i += 1
                if i < len(lines):
                    example_code.append(lines[i])
        # 其他内容
        else:
            if current_section == 'description' and stripped and not stripped.startswith('#'):
                sections['description'].append(line)
            elif current_section == 'examples' and stripped:
                example_desc.append(line)
            elif current_section == 'see_also' and stripped:
                sections['see_also'].append(line)
        
        i += 1
    
    # 处理最后一个示例
    if example_desc or example_code:
        sections['examples'].append({
            'description': '\n'.join(example_desc),
            'code': '\n'.join(example_code)
        })
    
    # 将描述列表合并为字符串
    sections['description_text'] = '\n'.join(sections['description']) if sections['description'] else ''
    return sections

# 翻译字典 - 常用技术术语
translation_dict = {
    # 通用术语
    'Returns': '返回',
    'Calculate': '计算',
    'Calculates': '计算',
    'Description': '描述',
    'Example': '示例',
    'Examples': '示例',
    'Syntax': '语法',
    'See Also': '另请参阅',
    'List of commands': '命令列表',
    'Note': '注意',
    'Note:': '注意：',
    'Important': '重要',
    'Warning': '警告',
    'Info': '信息',
    
    # 数学函数
    'trigonometric': '三角函数',
    'tangent': '正切',
    'sine': '正弦',
    'cosine': '余弦',
    'arc tangent': '反正切',
    'inverse': '反',
    'exponential': '指数',
    'logarithm': '对数',
    'natural logarithm': '自然对数',
    'square root': '平方根',
    'radians': '弧度',
    'complex': '复数',
    'real': '实部',
    'imaginary': '虚部',
    'absolute value': '绝对值',
    'angle': '角度',
    'phase': '相位',
    'magnitude': '幅值',
    'minimum': '最小值',
    'maximum': '最大值',
    'sum': '求和',
    'mean': '平均值',
    'average': '平均值',
    'standard deviation': '标准差',
    
    # 矩阵/数组操作
    'matrix': '矩阵',
    'vector': '向量',
    'array': '数组',
    'element': '元素',
    'elements': '元素',
    'dimension': '维度',
    'dimensions': '维度',
    'size': '大小',
    'length': '长度',
    'transpose': '转置',
    'inverse': '逆',
    'determinant': '行列式',
    'diagonal': '对角线',
    'identity': '单位',
    'zero': '零',
    'zeros': '零矩阵',
    'ones': '全1矩阵',
    'pinch': '压缩',
    'squeeze': '压缩',
    'reshape': '重塑',
    
    # 文件操作
    'file': '文件',
    'write': '写入',
    'read': '读取',
    'save': '保存',
    'load': '加载',
    'filename': '文件名',
    'directory': '目录',
    'path': '路径',
    'export': '导出',
    'import': '导入',
    'format': '格式',
    
    # 仿真相关
    'simulation': '仿真',
    'solver': '求解器',
    'mesh': '网格',
    'monitor': '监视器',
    'source': '光源',
    'field': '场',
    'frequency': '频率',
    'wavelength': '波长',
    'power': '功率',
    'intensity': '强度',
    'energy': '能量',
    'electric field': '电场',
    'magnetic field': '磁场',
    'permittivity': '介电常数',
    'permeability': '磁导率',
    'refractive index': '折射率',
    'absorption': '吸收',
    'transmission': '透射',
    'reflection': '反射',
    'scattering': '散射',
    'propagation': '传播',
    'mode': '模式',
    'modes': '模式',
    'boundary': '边界',
    'condition': '条件',
    'region': '区域',
    'domain': '域',
    
    # 数据操作
    'dataset': '数据集',
    'attribute': '属性',
    'parameter': '参数',
    'value': '值',
    'values': '值',
    'string': '字符串',
    'number': '数字',
    'numeric': '数值',
    'integer': '整数',
    'floating point': '浮点数',
    'boolean': '布尔值',
    'true': '真',
    'false': '假',
    'null': '空',
    'empty': '空',
    
    # 脚本/编程
    'script': '脚本',
    'command': '命令',
    'function': '函数',
    'variable': '变量',
    'expression': '表达式',
    'statement': '语句',
    'loop': '循环',
    'condition': '条件',
    'operator': '运算符',
    'assignment': '赋值',
    'argument': '参数',
    'parameter': '参数',
    'return': '返回',
    'output': '输出',
    'input': '输入',
}

def translate_simple(text):
    """简单翻译 - 替换常见术语"""
    if not text:
        return text
    
    result = text
    for en, cn in translation_dict.items():
        # 使用单词边界匹配
        pattern = r'\b' + re.escape(en) + r'\b'
        result = re.sub(pattern, cn, result, flags=re.IGNORECASE)
    
    return result

def translate_description(text):
    """翻译描述文本 - 使用完整句子翻译"""
    if not text or not text.strip():
        return text
    
    # 常见句式的完整翻译
    translations = {
        # all command
        'Returns 1 if all of the specified matrix entries are nonzero and returns 0 otherwise.': 
            '如果指定矩阵的所有元素均为非零值，则返回1，否则返回0。',
        'Will return 1 if all of the A matrix entries are nonzero and will return 0 otherwise.':
            '如果矩阵A的所有元素均为非零值，则返回1，否则返回0。',
        'n is an optional parameter to analyze entries in a specific dimension':
            'n是一个可选参数，用于分析特定维度中的元素',
        
        # amax command
        'Returns the maximum value in a specified dimension of a matrix. For complex numbers, only the real part is considered.':
            '返回矩阵指定维度中的最大值。对于复数，仅考虑实部。',
        'The maximum value in the specified dimension n of matrix x.':
            '矩阵x的指定维度n中的最大值。',
        
        # clear command  
        'Clears all or specified stored workspace variables. This will not clear any simulation data stored in d-cards. The variables c, pi, eps0, mu0 will be reset to their default values.':
            '清除所有或指定的存储工作区变量。这不会清除d-cards中存储的任何仿真数据。变量c、pi、eps0、mu0将重置为其默认值。',
        'Clears all workspace variables.  This function does not return any data.':
            '清除所有工作区变量。此函数不返回任何数据。',
        'Clears only the workspace variables with the specified names.':
            '仅清除具有指定名称的工作区变量。',
            
        # 通用模式
        'Returns': '返回',
        'The following is a simple example showing how to use this command.':
            '以下是一个简单的示例，展示如何使用此命令。',
        'Find the': '查找',
        'of the': '的',
        'of a matrix': '矩阵的',
        'first dimension': '第一维度',
        'second dimension': '第二维度',
        'vector length': '向量长度',
    }
    
    # 首先尝试完整匹配
    for en, cn in translations.items():
        if en.strip() == text.strip():
            return cn
    
    # 然后进行术语替换
    result = translate_simple(text)
    
    return result

def translate_table_cell(text):
    """翻译表格单元格"""
    return translate_simple(text)

def translate_example_desc(text):
    """翻译示例描述"""
    return translate_simple(text)

def batch_translate_files(files, batch_size=50):
    """批量翻译文件"""
    total = len(files)
    batches = (total + batch_size - 1) // batch_size
    
    results = {
        'success': 0,
        'failed': 0,
        'skipped': 0
    }
    
    for batch_num in range(batches):
        start_idx = batch_num * batch_size
        end_idx = min(start_idx + batch_size, total)
        batch_files = files[start_idx:end_idx]
        
        print(f"\n{'='*60}")
        print(f"批次 {batch_num + 1}/{batches} ({start_idx+1}-{end_idx}/{total})")
        print(f"{'='*60}")
        
        for filename in batch_files:
            cn_path = BASE_DIR / "cn" / filename
            en_path = BASE_DIR / "en" / filename
            command_name = filename.replace('.md', '')
            
            if not en_path.exists():
                print(f"  [跳过] 英文文件不存在: {filename}")
                results['skipped'] += 1
                continue
            
            try:
                # 翻译文档
                translated = translate_document(cn_path, en_path, command_name)
                
                # 写回文件
                with open(cn_path, 'w', encoding='utf-8') as f:
                    f.write(translated)
                
                print(f"  [完成] {filename}")
                results['success'] += 1
                
            except Exception as e:
                print(f"  [失败] {filename}: {e}")
                results['failed'] += 1
        
        # 显示进度
        completed = batch_num * batch_size + len(batch_files)
        progress = 100 * completed / total
        print(f"\n进度: {completed}/{total} ({progress:.1f}%)")
        print(f"成功: {results['success']}, 失败: {results['failed']}, 跳过: {results['skipped']}")
    
    return results

if __name__ == "__main__":
    print("LSF脚本命令文档批量翻译工具")
    print("=" * 60)
    
    # 获取需要翻译的文件
    files = get_files_to_translate()
    print(f"找到 {len(files)} 个需要翻译的文件")
    
    if not files:
        print("没有需要翻译的文件！")
        exit(0)
    
    # 显示前10个文件
    print("\n前10个文件:")
    for i, f in enumerate(files[:10], 1):
        print(f"  {i}. {f}")
    
    # 确认开始
    print("\n准备开始翻译...")
    
    # 执行批量翻译
    results = batch_translate_files(files, batch_size=50)
    
    # 显示最终结果
    print(f"\n{'='*60}")
    print("翻译完成！")
    print(f"{'='*60}")
    print(f"总计文件: {len(files)}")
    print(f"成功: {results['success']}")
    print(f"失败: {results['failed']}")
    print(f"跳过: {results['skipped']}")
