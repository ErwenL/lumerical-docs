# Lumerical 文档质量标准和 AI 润色指南

## 概述

本文档定义了 Lumerical Lumapi 命令文档的质量标准和 AI 辅助润色流程。目标是确保所有文档具有一致性、技术准确性、可读性和实用性。

## 文档质量标准

### 1. 结构一致性

所有命令文档必须遵循以下结构：

```
# 命令名称

## 概述

## 语法

### Lumerical 脚本语言 (LSF)
```lumerical
命令语法
```

### Python API (Lumapi)
```python
命令语法
```

## 参数

## 返回值

## 示例

### 示例 1: [描述]
#### LSF 脚本
```lumerical
代码
```

#### Python API
```python
代码
```

## 注意事项

## 错误处理

## 相关命令

## 产品支持

## 版本历史

## 参考

---

*最后更新: YYYY-MM-DD*  
*文档版本: x.x*
```

### 2. 格式规范

#### 2.1 标题层级
- 一级标题: `# 命令名称`
- 二级标题: `## 章节名称`
- 三级标题: `### 子章节名称`
- 代码块标题: `#### 描述`

#### 2.2 代码块格式
```markdown
#### LSF 脚本
```lumerical
addfdtd;
set("x span", 2e-6);
```

#### Python API
```python
import lumapi
fdtd = lumapi.FDTD()
fdtd.addfdtd()
fdtd.set("x span", 2e-6)
```
```

#### 2.3 表格格式
```markdown
| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `x` | float | 0 | 中心坐标 (m) |
| `x span` | float | 1e-6 | X 方向跨度 (m) |
```

### 3. 内容质量标准

#### 3.1 技术准确性
- 所有命令语法必须准确
- 参数描述必须正确
- 示例代码必须可运行（在适当上下文中）
- 单位必须正确指定

#### 3.2 完整性
- 必须包含 LSF 和 Python API 两种语法
- 必须提供至少 2-4 个示例（基本、中级、高级）
- 必须涵盖常见使用场景和错误情况
- 必须列出相关命令

#### 3.3 可读性
- 使用清晰简洁的语言
- 避免过于技术化的术语，或提供解释
- 示例代码应有注释说明
- 复杂概念应分步骤解释

#### 3.4 实用性
- 示例应反映实际应用场景
- 应包含常见问题解决方案
- 应提供性能优化建议
- 应包含错误处理和调试技巧

## AI 润色流程

### 1. 初步检查清单

在提交 AI 润色前，人工检查以下项目：

- [ ] 文档结构符合模板
- [ ] 所有必要章节都存在
- [ ] 代码语法正确
- [ ] 参数描述完整
- [ ] 示例代码有注释
- [ ] 无拼写和语法错误

### 2. AI 润色提示模板

使用以下提示模板进行 AI 润色：

```
请检查以下 Lumerical 命令文档的质量并给出改进建议：

[粘贴文档内容]

请按照以下标准检查：
1. 结构一致性：是否符合标准模板？
2. 技术准确性：命令语法、参数描述、示例代码是否正确？
3. 完整性：是否包含所有必要信息？
4. 可读性：语言是否清晰？示例是否有注释？
5. 格式规范：标题层级、代码块、表格格式是否正确？

请提供：
1. 问题列表（如果有）
2. 改进建议
3. 润色后的完整文档
```

### 3. AI 模型选择指南

根据文档复杂度选择 AI 模型：

| 文档类型 | 推荐模型 | 检查重点 |
|----------|----------|----------|
| 简单命令 | GPT-4/Claude 3 | 语法、格式、基础准确性 |
| 复杂命令 | GPT-4 Turbo/Claude 3.5 | 技术深度、高级示例、性能考虑 |
| 概念文档 | Claude 3.5 Sonnet | 概念准确性、逻辑连贯性、教学价值 |
| 参考手册 | 多模型交叉验证 | 全面性、一致性、技术细节 |

### 4. 润色后验证

AI 润色后必须进行以下验证：

#### 4.1 技术验证
- [ ] 命令语法与官方文档一致
- [ ] 参数名称和类型正确
- [ ] 示例代码在 Lumerical 中可运行（概念验证）
- [ ] 单位转换正确

#### 4.2 一致性验证
- [ ] 与其他命令文档格式一致
- [ ] 术语使用一致
- [ ] 代码风格一致
- [ ] 参考格式一致

#### 4.3 可读性验证
- [ ] 语言流畅自然
- [ ] 技术术语有解释
- [ ] 示例有充分注释
- [ ] 复杂概念分步骤解释

## 具体检查要点

### 1. 命令语法检查
- LSF 语法是否正确？
- Python API 语法是否正确？
- 参数顺序是否正确？
- 返回值描述是否准确？

### 2. 示例代码检查
- 示例是否完整（包含必要的导入和初始化）？
- 示例是否有注释说明每步作用？
- 示例是否反映实际应用场景？
- 示例是否包含错误处理？

### 3. 参数表检查
- 是否包含所有重要参数？
- 参数类型是否准确？
- 默认值是否正确？
- 描述是否清晰？

### 4. 注意事项检查
- 是否包含常见陷阱？
- 是否提供性能建议？
- 是否包含最佳实践？
- 是否说明限制条件？

### 5. 错误处理检查
- 是否列出常见错误？
- 是否提供解决方案？
- Python 错误处理示例是否正确？
- 是否包含调试建议？

## 质量评分标准

每个文档按以下标准评分（1-5 分）：

### 技术准确性（权重: 40%）
- 5: 完全准确，无技术错误
- 4: 轻微不准确，不影响使用
- 3: 有明显技术错误
- 2: 多个技术错误
- 1: 严重技术错误

### 完整性（权重: 25%）
- 5: 包含所有必要信息
- 4: 缺少少量非关键信息
- 3: 缺少重要信息
- 2: 信息严重不全
- 1: 信息极度不全

### 可读性（权重: 20%）
- 5: 非常清晰，易于理解
- 4: 基本清晰，有改进空间
- 3: 部分内容难以理解
- 2: 多数内容难以理解
- 1: 完全难以理解

### 实用性（权重: 15%）
- 5: 非常实用，直接可用
- 4: 比较实用，需要调整
- 3: 实用性一般
- 2: 实用性有限
- 1: 完全不实用

### 总分计算
```
总分 = (技术准确性×0.4) + (完整性×0.25) + (可读性×0.2) + (实用性×0.15)
```

### 质量等级
- A (4.0-5.0): 优秀，可直接发布
- B (3.0-3.9): 良好，需要少量改进
- C (2.0-2.9): 及格，需要显著改进
- D (1.0-1.9): 不及格，需要重写

## 文档维护流程

### 1. 新文档创建流程
1. 作者创建初始文档
2. 自检（使用初步检查清单）
3. AI 润色
4. 技术验证
5. 一致性验证
6. 可读性验证
7. 质量评分
8. 发布

### 2. 现有文档更新流程
1. 识别需要更新的部分
2. 更新内容
3. AI 润色更新部分
4. 验证整体一致性
5. 更新版本号和日期
6. 发布

### 3. 定期审查流程
- 每季度审查所有文档
- 检查技术过时内容
- 更新示例代码
- 统一格式改进
- 重新评分

## AI 润色工具和脚本

### 1. 自动化检查脚本
```python
#!/usr/bin/env python3
"""
Lumerical 文档自动检查脚本
检查文档结构、格式、完整性
"""

import re
import os
from pathlib import Path

def check_document_structure(file_path):
    """检查文档结构是否符合标准"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = {
        'has_title': bool(re.search(r'^#\s+.+', content, re.MULTILINE)),
        'has_overview': bool(re.search(r'^##\s+概述', content, re.MULTILINE)),
        'has_syntax': bool(re.search(r'^##\s+语法', content, re.MULTILINE)),
        'has_parameters': bool(re.search(r'^##\s+参数', content, re.MULTILINE)),
        'has_examples': bool(re.search(r'^##\s+示例', content, re.MULTILINE)),
        'has_lsf_example': bool(re.search(r'#### LSF 脚本', content)),
        'has_python_example': bool(re.search(r'#### Python API', content)),
    }
    
    return checks

def check_code_blocks(file_path):
    """检查代码块格式"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查代码块语言标识
    code_blocks = re.findall(r'```(\w+)', content)
    
    return {
        'total_code_blocks': len(code_blocks),
        'lumerical_blocks': code_blocks.count('lumerical'),
        'python_blocks': code_blocks.count('python'),
        'has_mixed_code': 'lumerical' in code_blocks and 'python' in code_blocks,
    }

# 使用示例
if __name__ == '__main__':
    docs_dir = Path('docs/lumapi')
    for md_file in docs_dir.glob('*.md'):
        print(f"\n检查文件: {md_file.name}")
        structure = check_document_structure(md_file)
        code_info = check_code_blocks(md_file)
        
        print("结构检查:", structure)
        print("代码块检查:", code_info)
```

### 2. AI 润色 API 集成
```python
import openai
import os

def polish_document_with_ai(document_content, model="gpt-4"):
    """
    使用 AI 润色文档
    
    Args:
        document_content: 文档内容
        model: AI 模型
    
    Returns:
        润色后的文档
    """
    prompt = f"""
请检查以下 Lumerical 命令文档的质量并给出改进建议：

{document_content}

请按照以下标准检查：
1. 结构一致性：是否符合标准模板？
2. 技术准确性：命令语法、参数描述、示例代码是否正确？
3. 完整性：是否包含所有必要信息？
4. 可读性：语言是否清晰？示例是否有注释？
5. 格式规范：标题层级、代码块、表格格式是否正确？

请提供润色后的完整文档。
"""
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是一个技术文档专家，专门检查 Lumerical 仿真软件文档质量。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=4000
    )
    
    return response.choices[0].message.content
```

## 常见问题解决方案

### 1. 技术准确性不足
**问题**: AI 可能生成技术上不准确的示例
**解决方案**: 
- 提供官方文档作为参考
- 要求 AI 引用具体版本信息
- 人工验证关键代码片段

### 2. 格式不一致
**问题**: 不同 AI 运行产生不同格式
**解决方案**:
- 提供详细格式模板
- 使用自动化格式化工具
- 建立格式检查清单

### 3. 语言风格不一致
**问题**: 文档间语言风格差异大
**解决方案**:
- 定义统一术语表
- 建立写作风格指南
- 使用同一次 AI 会话处理相关文档

### 4. 示例代码不可运行
**问题**: 示例缺少上下文
**解决方案**:
- 要求完整可运行示例
- 包含必要的导入和初始化
- 添加注释说明依赖关系

## 术语表

| 术语 | 定义 | 使用规范 |
|------|------|----------|
| LSF | Lumerical Script Language | 首字母大写，指 Lumerical 脚本语言 |
| Lumapi | Lumerical Python API | 首字母大写，指 Python API |
| FDTD | Finite-Difference Time-Domain | 全大写，指时域有限差分方法 |
| FDE | Finite-Difference Eigenmode | 全大写，指频域有限差分本征模式求解器 |
| EME | Eigenmode Expansion | 全大写，指本征模式扩展方法 |
| PML | Perfectly Matched Layer | 全大写，指完全匹配层边界条件 |

## 参考资源

### 1. 官方文档
- Lumerical Script Language Reference
- Lumerical Python API Documentation
- Lumerical Knowledge Base

### 2. 质量保证工具
- Markdown linting tools
- Code syntax checkers
- Spell checkers

### 3. AI 工具
- OpenAI GPT models
- Anthropic Claude models
- Local LLMs for sensitive content

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2025-01-30 | 初始版本 |

---

*最后更新: 2025-01-30*  
*文档版本: 1.0*