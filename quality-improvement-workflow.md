# LSF 脚本文档质量改进工作流程

## 概述

本工作流程旨在将部分翻译的LSF脚本命令文档（混合中英文）改进为高质量的中文翻译文档。当前项目中有**539个部分翻译文档**需要质量改进。

## 质量等级定义

### 1. 低质量文档（部分翻译）
- 混合中英文内容
- 句子结构仍然是英文
- 关键术语未翻译
- 可读性差
- **数量：539个文件**

### 2. 高质量文档（良好翻译）
- 完整的中文翻译
- 自然的句子结构
- 技术术语准确一致
- 格式规范
- **数量：188个文件**

### 3. 优秀文档标准
- ✅ 100%中文内容（代码块除外）
- ✅ 自然的句子结构
- ✅ 技术术语翻译准确一致
- ✅ 格式符合项目规范
- ✅ 链接正确指向本地文档
- ✅ 代码块和示例保留原样

## 工作流程设计

### 第1步：评估与规划

#### 1.1 识别需要改进的文件
```bash
# 运行质量检查脚本
python scripts/check_translation_status.py

# 获取部分翻译文件列表
python scripts/check_translation_status.py 2>&1 | grep "部分翻译" -A 5
```

#### 1.2 优先级排序策略
1. **高频使用命令优先**：数学函数、文件操作、仿真核心命令
2. **质量最差优先**：混合程度最高的文件
3. **功能分组优先**：按功能类别批量处理

#### 1.3 选择改进策略

| 策略 | 适用场景 | 优点 | 缺点 |
|------|----------|------|------|
| **完全手动改进** | 复杂技术文档，需要专业判断 | 质量最高，术语准确 | 速度慢，人力成本高 |
| **自动+手动检查** | 中等复杂度，有标准模板 | 效率高，一致性较好 | 需要人工检查调整 |
| **批量自动改进** | 简单文档，重复模式多 | 效率最高 | 质量可能不稳定 |

### 第2步：质量改进执行

#### 2.1 手动改进流程（推荐用于复杂文档）

**步骤1：准备工作**
```bash
# 查看英文原文
cat docs/lsf-script/en/<command>.md

# 查看当前中文翻译
cat docs/lsf-script/cn/<command>.md
```

**步骤2：逐句改进**
1. 复制英文原文到临时文件
2. 逐句翻译，确保：
   - 技术术语准确
   - 句子结构自然
   - 保持技术准确性

**步骤3：格式检查**
1. 标题格式：`# 命令名称`
2. 表格格式：使用标准Markdown表格
3. 代码块：使用三个反引号，保留原语言
4. 链接：转换为本地相对链接

#### 2.2 自动+手动检查流程（推荐用于多数文档）

**步骤1：运行自动改进脚本**
```bash
# 安装必要依赖
pip install -r requirements.txt

# 运行质量改进脚本
python scripts/quality_improvement.py --command <command> --strategy aggressive
```

**步骤2：手动检查与调整**
1. 检查自动翻译的准确性
2. 调整不自然的句子
3. 修正技术术语
4. 验证格式

#### 2.3 批量处理模式
```bash
# 批量改进10个文件
python scripts/quality_improvement.py --batch 10 --strategy balanced

# 按功能组处理
python scripts/quality_improvement.py --category math --batch 20
```

### 第3步：质量检查标准

#### 3.1 内容完整性检查表
- [ ] **技术准确性**：翻译准确传达原意
- [ ] **术语一致性**：同一术语在整个文档集中翻译一致
- [ ] **句子自然度**：中文表达流畅自然
- [ ] **完整性**：所有内容都已翻译（代码块除外）
- [ ] **格式规范**：符合Markdown格式要求

#### 3.2 技术术语检查
```python
# 必须翻译的术语示例
必需翻译 = {
    "adds": "添加",
    "returns": "返回", 
    "creates": "创建",
    "sets": "设置",
    "simulation": "仿真",
    "solver": "求解器",
    "monitor": "监视器",
    "material": "材料",
    "property": "属性",
    "parameter": "参数"
}

# 不应翻译的内容
不应翻译 = [
    命令名称,      # 如 "addmaterial"
    函数名,        # 如 "set", "get"
    代码变量,      # 如 "x", "y", "z"
    文件扩展名,    # 如 ".mat", ".csv"
    URL链接       # 完整URL保持不变
]
```

#### 3.3 格式验证清单
- [ ] 文件头包含翻译元数据
- [ ] 一级标题为命令名称
- [ ] 表格对齐正确
- [ ] 代码块语言标识正确
- [ ] 链接使用相对路径（`./command.md`）
- [ ] 中英文间有空格（如`LSF 脚本`）
- [ ] 中文使用全角标点（，。；：！？）

### 第4步：工具与自动化

#### 4.1 质量改进脚本 (`scripts/quality_improvement.py`)
```python
# 主要功能
- 识别混合翻译模式
- 应用术语翻译词典（500+术语）
- 重构句子结构
- 检查并修复格式问题
- 生成改进报告
```

#### 4.2 质量评估脚本 (`scripts/quality_assessment.py`)
```python
# 评估指标
- 中文覆盖率（中文字符比例）
- 术语一致性得分
- 句子自然度评分
- 格式合规性检查
- 链接有效性验证
```

#### 4.3 批量处理脚本 (`scripts/batch_quality_improvement.py`)
```bash
# 使用示例
# 处理前20个部分翻译文档
python scripts/batch_quality_improvement.py --start 0 --batch 20

# 按质量评分优先处理
python scripts/batch_quality_improvement.py --priority worst-first --batch 10

# 生成进度报告
python scripts/batch_quality_improvement.py --report
```

### 第5步：进度跟踪与验收

#### 5.1 进度跟踪文件 (`docs/quality-improvement-progress.json`)
```json
{
  "total_files": 539,
  "completed_files": 0,
  "in_progress_files": [],
  "pending_files": ["abs", "add2drect", ...],
  "quality_scores": {},
  "start_date": "2026-02-04",
  "last_update": "2026-02-04"
}
```

#### 5.2 验收标准
- **个人验收**：每个文件完成质量检查清单
- **批次验收**：每批文件（20个）完成后运行验证脚本
- **最终验收**：所有文件通过自动化质量检查

#### 5.3 验收检查脚本
```bash
# 检查单个文件质量
python scripts/verify_quality.py --file docs/lsf-script/cn/addanalysisgroup.md

# 检查批次质量
python scripts/verify_quality.py --batch 1 --threshold 0.8

# 生成质量报告
python scripts/verify_quality.py --report --output quality-report.md
```

### 第6步：试运行与评估

#### 6.1 试运行计划
1. **样本选择**：选择10个不同类型的部分翻译文档
2. **策略测试**：测试不同改进策略的效果
3. **效率评估**：记录处理每个文件的时间
4. **质量评估**：评估改进前后的质量差异

#### 6.2 效率指标
- **处理速度**：文件/小时
- **质量提升**：质量评分提升百分比
- **人工干预**：需要手动调整的比例
- **一致性**：术语翻译一致性

#### 6.3 质量评分体系
```python
质量评分 = {
    "中文覆盖率": 0.3,      # 中文字符比例
    "术语准确性": 0.3,      # 技术术语翻译正确率
    "句子自然度": 0.2,      # 句子结构自然程度
    "格式合规性": 0.2       # 格式规范符合度
}
```

### 第7步：规模化实施

#### 7.1 分批处理建议
- **小批次**：10-20个文件/批（质量控制最佳）
- **中批次**：50个文件/批（效率与质量平衡）
- **大批次**：100个文件/批（效率优先，需要严格质量检查）

#### 7.2 团队协作模式
- **个人负责制**：每人负责特定功能类别的文档
- **交叉检查**：完成批次后交叉检查质量
- **定期同步**：每周同步进度和质量问题

#### 7.3 质量控制点
1. **预处理检查**：改进前记录原始质量评分
2. **过程检查**：每5个文件检查一次术语一致性
3. **后处理检查**：改进后运行完整质量检查
4. **抽样审计**：随机抽样审计10%的改进文件

## 实施建议

### 短期目标（1-2周）
1. 完成工具脚本开发
2. 试运行并优化流程
3. 建立质量评估体系
4. 培训团队成员（如果需要）

### 中期目标（3-4周）
1. 完成50%的部分翻译文档改进（~270个文件）
2. 优化自动化工具基于实际使用反馈
3. 建立稳定的质量改进流水线

### 长期目标（6-8周）
1. 完成所有539个部分翻译文档改进
2. 建立持续质量监控机制
3. 文档整体质量达到优秀标准

## 附录

### A. 质量改进示例

**改进前（部分翻译）：**
```
添加 an [analysis group](/hc/en-us/articles/360034382454) to the 仿真 environment. Analysis groups are container 对象 that can contain any 仿真 对象 and associated 脚本 functions which can be used to 创建 customize 数据 analysis.
```

**改进后（高质量翻译）：**
```
向仿真环境中添加一个[分析组](/hc/en-us/articles/360034382454)。分析组是容器对象，可以包含任何仿真对象和相关的脚本函数，用于创建自定义数据分析。
```

### B. 常用命令参考

```bash
# 1. 检查当前质量状态
python scripts/check_translation_status.py

# 2. 获取需要改进的文件列表
python scripts/get_quality_improvement_list.py --limit 20

# 3. 改进单个文件
python scripts/quality_improvement.py --command addanalysisgroup

# 4. 批量改进文件
python scripts/batch_quality_improvement.py --batch 10

# 5. 验证改进质量
python scripts/verify_quality.py --file docs/lsf-script/cn/addanalysisgroup.md

# 6. 生成进度报告
python scripts/generate_quality_report.py --output quality-report.md
```

### C. 联系与支持

如有问题或需要调整工作流程，请参考：
1. 现有翻译工作流程指南：`docs/translation-workflow-guide.md`
2. 项目质量标准文档
3. 技术术语翻译表

---

*文档版本：1.0*  
*创建日期：2026-02-04*  
*更新者：AI Assistant*  
*预计工作量：539个文件，约80-120人时*