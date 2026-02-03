# LSF Script Documentation Translation Workflow Guide

## 概述

本指南详细说明了如何系统化地处理LSF脚本命令文档的翻译工作。每个英文文档需要完成以下四个任务：

1. **检查文档质量** - 确保格式、内容和链接符合标准
2. **修改"see also"部分** - 改为项目符号格式，并将链接指向本地文档
3. **翻译文档** - 将英文内容翻译成中文，保存在`/lsf-script/cn/`目录
4. **自动格式化** - 应用一致的格式规范

## 项目结构

```
docs/lsf-script/
├── en/          # 原始英文文档（727个文件）
├── cn/          # 中文翻译文档（目标目录）
├── lsf-script-commands-alphabetical.md   # 命令索引
└── missing-lsf-script-docs.md            # 缺失命令列表
```

## 工作流程

### 第1步：准备工作
1. 使用翻译辅助工具检查当前状态：
   ```bash
   python scripts/translation_helper.py --stats
   ```
2. 查看待处理命令列表：
   ```bash
   python scripts/translation_helper.py --list --limit 20
   ```
3. 记录起始点，以便中断后恢复。

### 第2步：文档质量检查标准

#### 格式要求
- **文件命名**：小写字母，使用连字符分隔单词（如`add-material.md`）
- **标题**：一级标题为命令名称（如`# addmaterial`）
- **代码块**：使用三个反引号，指定语言为`lumerical`或`matlab`
- **表格**：使用标准的Markdown表格语法
- **换行**：句子之间保持适当的换行，提高可读性

#### 内容完整性检查
- [ ] 命令描述完整
- [ ] 语法部分包含所有用法变体
- [ ] 示例代码正确且可运行
- [ ] 参数说明清晰
- [ ] "See Also"部分存在且相关

#### 链接检查
- [ ] 所有内部链接有效
- [ ] 外部链接指向正确的Ansys文档
- [ ] 没有损坏的链接

### 第3步："See Also"部分转换规则

#### 原始格式（需要转换）
```
**See Also**
[Related Command 1](https://optics.ansys.com/hc/en-us/articles/...)
[Related Command 2](https://optics.ansys.com/hc/en-us/articles/...)
```

#### 目标格式（转换后）
```markdown
**See Also**

- [Related Command 1](./related-command-1.md)
- [Related Command 2](./related-command-2.md)
```

#### 转换规则
1. 将"See Also"标题保持为`**See Also**`（粗体）
2. 添加一个空行
3. 使用项目符号列表（`- `开头）
4. 将Ansys链接转换为本地相对链接：
   - 提取命令名称从URL中（如`https://.../articles/...-command-name` → `command-name`）
   - 创建相对路径`./command-name.md`
   - 如果命令名包含特殊字符，使用已清理的文件名
5. 保持链接文本的描述性

### 第4步：翻译指南

#### 技术术语翻译表
| 英文术语 | 中文翻译 | 备注 |
|---------|---------|------|
| syntax | 语法 | |
| description | 描述 | |
| example | 示例 | |
| parameter | 参数 | |
| argument | 参数 | |
| return value | 返回值 | |
| property | 属性 | |
| monitor | 监视器 | |
| solver | 求解器 | |
| material | 材料 | |
| simulation | 仿真 | |
| script | 脚本 | |
| function | 函数 | |
| command | 命令 | |
| structure | 结构 | |
| database | 数据库 | |

#### 翻译原则
1. **准确性优先**：技术文档必须准确传达原意
2. **一致性**：同一术语在整个文档集中保持一致
3. **可读性**：中文表达自然流畅，避免生硬直译
4. **简洁性**：在保持准确的前提下尽量简洁
5. **格式保留**：保持原有的Markdown格式、代码块和表格

#### 特殊处理
- **代码部分**：不翻译，保持原样
- **命令名称**：不翻译，保持英文
- **技术参数名**：不翻译，保持英文
- **URL链接**：不翻译，保持原样
- **数学公式**：不翻译，保持原样

### 第5步：自动格式化规范

#### 英文文档格式化
1. 使用统一的标题层级
2. 代码块使用正确的语言标识
3. 表格对齐一致
4. 列表缩进统一（2个空格）
5. 行长度限制在80个字符以内（除代码块外）

#### 中文文档格式化
1. 中英文之间添加空格（如`LSF 脚本`）
2. 中文标点使用全角符号（，。；：！？）
3. 数字和英文单词使用半角字符
4. 专有名词不添加空格（如`MATLAB`）

### 第6步：批量处理策略

#### 分批处理
建议每次处理10-20个文件，以确保质量可控。

#### 进度跟踪文件
创建`docs/translation-progress-detailed.json`跟踪详细进度：
```json
{
  "last_processed": "addmaterial",
  "processed_count": 1,
  "total_count": 727,
  "processed_files": ["addmaterial"],
  "pending_files": ["abs", "acos", ...],
  "last_update": "2026-02-03T00:00:00Z"
}
```

#### 恢复机制
如果工作中断，可以通过以下步骤恢复：
1. 检查进度跟踪文件，找到最后处理的命令
2. 从下一个命令继续处理
3. 使用翻译辅助工具验证已处理文件

### 第7步：并行工作流程

当有多个团队或工作者同时进行翻译工作时，需要使用并行工作流程来避免重复劳动并有效协调进度。

#### 并行工作优势
- **提高效率**：多个section同时处理，缩短总体完成时间
- **负载均衡**：工作量均匀分配，避免单个团队过载
- **灵活调度**：团队可根据进度动态调整

#### Section调度系统
使用`section_scheduler.py`工具进行任务分配：

```bash
# 分析命令分布
python scripts/section_scheduler.py analyze

# 创建4个均衡的section（默认策略）
python scripts/section_scheduler.py create --sections 4

# 使用字母分组策略
python scripts/section_scheduler.py create --sections 4 --strategy letter

# 使用自定义字母范围
python scripts/section_scheduler.py create --custom-ranges "A-D,E-H,I-L,M-P,Q-T,U-Z"
```

#### Section分配策略
1. **均衡分配（推荐）**：每个section包含大致相同数量的命令
   - 优点：工作量均匀，进度可预测
   - 缺点：命令可能来自不同字母，缺乏连续性

2. **字母分组分配**：按字母范围分组命令
   - 优点：命令有连续性，便于管理
   - 缺点：工作量可能不均衡（如"A"开头的命令较多）

3. **自定义范围分配**：手动指定字母范围
   - 优点：完全控制分配
   - 缺点：需要手动平衡工作量

#### 避免重复的协调机制
1. **预分配机制**：每个命令只属于一个section，从根本上避免重复
2. **进度锁定**：完成命令后立即更新section进度
3. **中央跟踪**：所有section进度集中跟踪在`docs/translation-sections/`目录

#### 并行工作流程
1. **初始化分配**：
   ```bash
   python scripts/section_scheduler.py create --sections 4
   ```
   生成4个section文件在`docs/translation-sections/`目录

2. **团队分配**：
   - 每个团队负责一个section（如Team 1 → Section 1）
   - 团队内部可进一步分工处理section内的命令

3. **处理单个命令**（标准流程）：
   - 检查英文文档质量
   - 修改"See Also"链接为本地相对链接
   - 翻译文档内容
   - 应用格式化

4. **更新进度**：
   ```bash
   # 完成一个命令后更新对应section
    python scripts/section_scheduler.py update --section 1 --completed addcustom
   ```

5. **监控整体进度**：
   ```bash
   python scripts/section_scheduler.py progress
   ```

#### Section文件结构
```
docs/translation-sections/
├── section_1.json          # Section 1的任务列表和进度
├── section_2.json          # Section 2的任务列表和进度
├── section_3.json          # Section 3的任务列表和进度
├── section_4.json          # Section 4的任务列表和进度
├── sections_overview.json  # 所有section的概览
└── WORK_ASSIGNMENT_GUIDE.md # 工作分配指南
```

#### Section进度文件示例
```json
{
  "section_id": "1",
  "commands": ["addcustom", "adddeltachargesource", ...],
  "command_count": 177,
  "completed_commands": ["addcustom", "adddeltachargesource"],
  "progress": 1.13,
  "status": "in_progress",
  "created_date": "2026-02-03T08:29:38.821443"
}
```

#### 团队内部协调
如果一个section由多个工作者处理，建议：
1. **内部任务分配**：团队负责人将section内的命令分配给成员
2. **批次处理**：每个成员处理5-10个命令为一组
3. **定期同步**：团队内部定期同步进度，避免内部重复

#### 冲突处理
虽然预分配机制避免了section间的重复，但仍需注意：
1. **文件冲突**：多人同时编辑同一文件时可能冲突
2. **进度更新冲突**：同时更新同一section进度可能冲突
3. **解决方案**：
   - 使用版本控制系统（Git）管理文件更改
   - 定期拉取最新更改
   - 协调进度更新频率

#### 进度整合
所有section完成后，翻译工作即完成。系统会自动跟踪整体进度，无需手动合并。

### 第8步：质量保证

#### 自查清单（每个文件）
- [ ] 英文文档质量检查通过
- [ ] "See Also"部分已转换
- [ ] 翻译准确且完整
- [ ] 中文文档格式正确
- [ ] 链接指向正确的本地文件
- [ ] 技术术语翻译一致

#### 批量验证
每完成一批文件（20个），运行验证脚本：
```bash
python scripts/verify_translation_batch.py --batch 1
```

### 第9步：实用工具和命令

#### 翻译辅助工具
```bash
# 查看统计
python scripts/translation_helper.py --stats

# 列出待处理命令
python scripts/translation_helper.py --list --limit 20

# 准备翻译模板
python scripts/translation_helper.py --prepare <command>

# 生成详细报告
python scripts/translation_helper.py --report
```

#### 进度更新脚本
```bash
# 更新进度跟踪
python scripts/update_translation_progress.py --command <command> --status completed
```

### 第10步：常见问题处理

#### 问题1：找不到对应的本地文档
- **现象**："See Also"中的命令在本地没有对应文档
- **处理**：暂时保持原始链接，添加注释`<!-- TODO: 需要添加本地文档 -->`

#### 问题2：特殊字符命令
- **现象**：命令名包含特殊字符（如`+`, `-`, `*`等）
- **处理**：使用已清理的文件名（如`plus.md`, `minus.md`, `asterisk.md`）

#### 问题3：翻译不确定
- **现象**：技术术语没有标准翻译
- **处理**：保持英文术语，添加括号注释说明（如`material（材料）`）

#### 问题4：格式不一致
- **现象**：原始文档格式差异较大
- **处理**：应用统一的格式化模板，确保一致性

### 第11步：完成标准

#### 短期目标（每批）
- [ ] 10-20个文件处理完成
- [ ] 质量自查通过
- [ ] 进度跟踪更新
- [ ] 验证脚本运行通过

#### 长期目标（全部）
- [ ] 727个英文文档全部检查完成
- [ ] 所有"See Also"链接转换完成
- [ ] 所有中文翻译完成
- [ ] 所有文档格式化完成
- [ ] 最终验证通过

## 附录

### 参考文档
1. [LSF Script Commands Alphabetical](./lsf-script-commands-alphabetical.md)
2. [Documentation Quality Standards](./documentation-quality-standards.md)
3. [Translation Progress](./translation-progress.json)

### 模板文件
英文文档模板和中文文档模板可在`samples/`目录中找到。

### 联系信息
如有问题或需要澄清，请参考项目文档或创建issue。

---
*文档版本: 1.1*  
*最后更新: 2026-02-03*  
*更新者: AI Assistant*