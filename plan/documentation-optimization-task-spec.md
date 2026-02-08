# Lumerical文档质量优化任务规范

## 项目概述

### 背景
本项目旨在优化Lumerical脚本命令文档的质量，包括：
1. **文档链接优化**：更新相对路径链接为可点击的完整URL或本地相对链接
2. **格式统一**：使用mdformat对所有Markdown文档进行格式化
3. **索引文件转换**：将命令列表转换为表格格式，提供更好的可读性

### 当前状态
- **英文文档数量**：727个（位于 `docs/lsf-script/en/`）
- **命令索引文件**：`docs/lsf-script/lsf-script-commands-alphabetical.md`（列表格式）
- **文档质量问题**：
  - 98.9%文档使用相对路径链接（`/hc/en-us/articles/...`）
  - "See Also"部分链接格式不一致
  - 缺少统一的格式化

---

## 技术分析结果

### 1. 文件名编码规则

通过对727个文档文件名的分析，确定了以下编码规则：

#### 特殊字符替换映射表
| 特殊字符/序列 | 文件名编码 | 示例 |
|---------------|------------|------|
| `.` | `dot` | `.` → `dot.md` |
| `(` | `lparen` | `(` → `lparen` |
| `)` | `rparen` | `)` → `rparen` |
| `!=` | `exclamationequals` | `!=` → `exclamationequals.md` |
| `<=` | `lte` | `<=` → `lte.md` |
| `>=` | `gte` | `>=` → `gte.md` |
| `==` | `equalequal` | `==` → `equalequal.md` |
| `!` | `exclamation` | `!` → `exclamation.md` |
| `*` | `asterisk` | `*` → `asterisk.md` |
| `+` | `plus` | `+` → `plus.md` |
| `-` | `minus` | `-` → `minus.md` |
| `/` | `slash` | `/` → `slash.md` |
| `:` | `colon` | `:` → `colon.md` |
| `<` | `lt` | `<` → `lt.md` |
| `=` | `equals` | `=` → `equals.md` |
| `>` | `gt` | `>` → `gt.md` |
| `?` | `question` | `?` → `question.md` |
| `[` | `lbracketrbracket` | `[` → `lbracketrbracket.md` |
| `^` | `caret` | `^` → `caret.md` |
| `|` | `pipe` | `|` → `pipe.md` |
| `~` | `tilde` | `~` → `tilde.md` |
| ` ` (空格) | `_` | `addport (FDTD)` → `addport_lparenFDTDrparen.md` |

#### 异常情况
- **点号冲突**：`.md`文件对应点号命令，`dot_cmd.md`对应`dot`命令（点积运算）
- **唯一冲突**：仅`dot`命令需要`_cmd`后缀避免文件名冲突

#### Python编码函数
```python
def command_to_filename(cmd: str) -> str:
    """将Lumerical命令名转换为文档文件名"""
    special_cases = {'dot': 'dot_cmd', '.': 'dot', '[': 'lbracketrbracket'}
    if cmd in special_cases:
        return special_cases[cmd]
    
    replacements = [
        ('!=', 'exclamationequals'), ('<=', 'lte'), ('>=', 'gte'), ('==', 'equalequal'),
        (' ', '_'), ('(', 'lparen'), (')', 'rparen'),
        # ... 其他单字符替换
    ]
    result = cmd
    for old, new in replacements:
        result = result.replace(old, new)
    return result
```

### 2. 链接模式分析

#### 主要链接模式
1. **命令文档链接**：`/hc/en-us/articles/{文章ID}-{命令名}`
   - 示例：`/hc/en-us/articles/360034925553-abs`
   - 处理策略：转换为本地相对链接 `./{文件名}.md`

2. **命令列表链接**：`/hc/en-us/articles/360037228834`
   - 出现次数：519次（在727个文档中）
   - 处理策略：转换为本地索引文件 `../lsf-script-commands-alphabetical.md`

3. **非命令文章链接**：教程、概念文档等
   - 示例：`/hc/en-us/articles/360034394634-Material-Permittivity-Models`
   - 处理策略：补全为完整URL `https://optics.ansys.com/hc/en-us/articles/...`

4. **相对路径链接**：
   - 旧格式：逗号分隔的绝对链接
   - 新格式：列表项形式的相对链接

---

## 优化目标

### 主要目标
1. **链接可达性**：所有链接可点击且指向正确位置
2. **格式一致性**：所有文档使用统一的Markdown格式
3. **索引可读性**：命令列表转换为表格格式，提供更好的导航

### 成功标准
- [ ] 100%文档中的相对路径链接已转换为可点击链接
- [ ] 所有命令链接指向本地对应文档
- [ ] 命令索引文件转换为三列表格格式
- [ ] 所有文档通过mdformat格式化
- [ ] 所有外部链接经过有效性验证（HTTP HEAD检查）

---

## 详细实施计划

### 阶段1：备份与准备 ✅
- **时间估算**：15分钟
- **关键任务**：
  1. 创建Git备份标签：`pre-optimization-2026-02-08`
  2. 创建本地备份目录：`backup/en_backup_20260208/`
  3. 验证备份完整性（文件数量、大小校验）

- **输出**：
  - Git标签备份
  - 本地文件备份
  - 备份验证报告

### 阶段2：开发优化脚本 ✅
- **时间估算**：2小时
- **关键任务**：
  1. 开发 `scripts/optimize_documentation.py`
  2. 实现四个核心模块：
     - `CommandMapper`：构建命令名↔文件名↔URL映射
     - `LinkUpdater`：智能识别和转换链接
     - `IndexTransformer`：生成三列表格索引
     - `Formatter`：使用mdformat统一格式化
  3. 添加验证和回滚模块

- **模块功能**：

#### CommandMapper 类
```python
class CommandMapper:
    """构建命令名、文件名和URL之间的映射关系"""
    def build_mapping() -> Dict[str, Dict[str, str]]:
        # 从索引文件提取命令名→URL映射
        # 从文件名反向工程命令名→文件名映射
        # 返回：{'abs': {'filename': 'abs.md', 'url': 'https://...'}}
```

#### LinkUpdater 类
```python
class LinkUpdater:
    """智能识别和转换Markdown文档中的链接"""
    LINK_PATTERNS = {
        "command": r"/hc/en-us/articles/\d+-[a-zA-Z0-9_-]+",
        "list_of_commands": r"/hc/en-us/articles/360037228834",
        "article": r"/hc/en-us/articles/\d+-[A-Z][a-z]+",
        "category": r"/hc/en-us/categories/",
    }
    
    def update_file(filepath: Path) -> bool:
        # 识别并转换所有链接
        # 返回：是否成功更新
```

#### IndexTransformer 类
```python
class IndexTransformer:
    """将命令列表文件转换为三列表格格式"""
    def convert_to_table() -> str:
        # 转换格式
        # 保持字母分组结构
        # 输出三列表格：命令名 | 官方链接 | 本地链接
```

#### Formatter 类
```python
class Formatter:
    """使用mdformat统一格式化所有文档"""
    def format_all() -> bool:
        # 批量格式化所有.md文件
        # 检查格式化结果
```

### 阶段3：小样本测试
- **时间估算**：30分钟
- **关键任务**：
  1. 选取10个代表性文档进行测试
  2. 验证链接转换逻辑
  3. 验证文件名映射准确性
  4. 测试mdformat格式化效果

- **测试文档选择标准**：
  - 常规命令：`abs.md`, `addmaterial.md`
  - 特殊字符命令：`dot_cmd.md`, `addport_lparenFDTDrparen.md`
  - 包含多种链接类型的文档
  - "See Also"部分格式多样的文档

### 阶段4：批量处理
- **时间估算**：3-4小时
- **关键任务**：
  1. 分批处理（每批50个文件，共15批）
  2. 实现断点续传机制
  3. 生成实时进度报告
  4. 记录详细的处理日志

#### 断点续传机制
```python
# 检查点文件结构
checkpoint = {
    "start_time": "2026-02-08T10:30:00",
    "total_files": 727,
    "processed_files": 350,
    "current_batch": 7,
    "failed_files": [],
    "last_successful_file": "getmaterial.md"
}
```

#### 批次处理配置
```python
BATCH_CONFIG = {
    "batch_size": 50,
    "checkpoint_file": "optimization_checkpoint.json",
    "progress_file": "optimization_progress.json",
    "error_log": "optimization_errors.json",
}
```

### 阶段5：索引文件转换
- **时间估算**：30分钟
- **关键任务**：
  1. 读取现有列表格式索引文件
  2. 转换为三列表格格式
  3. 保持字母分组结构
  4. 添加超链接（官方URL + 本地文件）

#### 表格格式示例
```markdown
| 命令名 | 官方文档 | 本地文档 |
|--------|----------|----------|
| [abs](./abs.md) | [链接](https://optics.ansys.com/hc/en-us/articles/360034925553-abs) | [abs.md](./abs.md) |

### 按字母分组

#### A
（保持现有分组结构）
```

### 阶段6：验证与报告
- **时间估算**：1小时
- **关键任务**：
  1. 随机抽样验证（5%文档，约36个文件）
  2. 链接有效性检查（所有外部链接）
  3. 生成优化报告
  4. 清理临时文件

#### 链接有效性检查
```python
async def check_link(url: str) -> LinkStatus:
    """异步检查链接有效性"""
    # HTTP HEAD请求（轻量级检查）
    # 超时设置：10秒
    # 重试机制：3次
    # 返回状态：valid, timeout, redirect, error
```

#### 验证报告结构
```json
{
  "summary": {
    "total_files": 727,
    "processed_files": 727,
    "links_updated": 3456,
    "formatting_errors": 0,
    "invalid_links": []
  },
  "details": {
    "link_conversions": {
      "command_links": 1234,
      "list_of_commands": 519,
      "external_articles": 1703
    },
    "validation_results": {
      "files_validated": 36,
      "links_checked": 180,
      "invalid_links": []
    }
  }
}
```

---

## 验证机制

### 1. 链接有效性检查
- **检查范围**：所有文档中的所有外部链接
- **检查方法**：异步HTTP HEAD请求
- **超时设置**：10秒
- **重试机制**：3次
- **结果记录**：无效链接记录到验证报告

### 2. 映射准确性验证
- **文件名映射**：验证所有命令名↔文件名的双向映射
- **链接映射**：验证命令链接是否正确指向本地文件
- **交叉引用**：检查文档间的互相引用一致性

### 3. 格式化验证
- **语法检查**：使用mdformat检查Markdown语法
- **格式一致性**：验证所有文档的格式统一性
- **特殊内容保留**：确保数学公式、代码块等特殊内容不被破坏

### 4. 抽样验证策略
- **抽样比例**：5%（约36个文档）
- **选择方法**：分层随机抽样（按字母分组）
- **验证内容**：链接转换、格式、内容完整性

---

## 风险控制与备份策略

### 风险评估
| 风险 | 概率 | 影响 | 缓解措施 |
|------|------|------|----------|
| 链接转换错误 | 中 | 高 | 小样本测试，验证机制 |
| 格式化破坏内容 | 低 | 高 | 备份，内容校验 |
| 网络请求超时 | 高 | 中 | 异步处理，超时重试 |
| 内存不足 | 低 | 高 | 分批处理，垃圾回收 |
| 意外中断 | 中 | 高 | 断点续传，检查点 |

### 备份策略
1. **Git备份**：
   - 创建标签：`pre-optimization-2026-02-08`
   - 描述：优化前的完整状态

2. **文件系统备份**：
   - 备份目录：`backup/en_backup_20260208/`
   - 包含：所有.md文件，索引文件
   - 校验：文件数量和大小验证

3. **增量备份**：
   - 每批处理后创建检查点
   - 检查点包含处理状态和错误信息

### 回滚机制
```python
def rollback_to_backup(backup_dir: Path):
    """回滚到备份状态"""
    # 1. 删除当前所有.md文件
    # 2. 从备份目录恢复文件
    # 3. 恢复索引文件
    # 4. 验证恢复完整性
```

---

## 技术架构

### 脚本架构
```
optimize_documentation.py
├── main()
├── CommandMapper (构建映射)
├── LinkUpdater (链接转换)
├── IndexTransformer (索引转换)
├── Formatter (格式化)
├── Validator (验证)
├── BackupManager (备份管理)
└── CheckpointManager (断点续传)
```

### 依赖关系
```toml
# pyproject.toml 中的相关依赖
dependencies = [
    "beautifulsoup4>=4.14.3",
    "cloudscraper>=1.2.71",
    "requests>=2.32.5",
    "aiohttp>=3.9.0",  # 异步HTTP客户端
    "mdformat>=0.7.0",
    "mdformat-tables>=0.4.0",
]
```

### 性能优化
1. **异步处理**：使用asyncio进行并发链接检查
2. **分批处理**：每批50个文件，控制内存使用
3. **缓存机制**：缓存映射关系，避免重复计算
4. **进度反馈**：实时显示处理进度和估计剩余时间

---

## 预期输出

### 文档优化成果
1. **可点击的链接**：所有文档中的链接都可直接点击访问
2. **统一的格式**：所有文档使用一致的Markdown格式
3. **增强的索引**：三列表格格式的命令索引
4. **验证报告**：详细的优化过程和结果报告

### 文件结构变化
```
docs/lsf-script/
├── en/ (优化后的英文文档)
│   ├── abs.md (链接已更新，格式统一)
│   ├── addmaterial.md
│   └── ...
├── lsf-script-commands-alphabetical.md (三列表格格式)
└── optimization-report.json (优化报告)
```

### 质量指标
| 指标 | 优化前 | 优化后 | 目标 |
|------|--------|--------|------|
| 不可点击链接 | 98.9% | 0% | 100%可点击 |
| 格式一致性 | 低 | 高 | 100%统一 |
| 链接有效性 | 未知 | 已验证 | 95%以上有效 |
| 索引可读性 | 列表 | 表格 | 三列表格 |

---

## 时间估算与资源需求

### 时间估算
| 阶段 | 时间估算 | 关键依赖 |
|------|----------|----------|
| 阶段1：备份与准备 | 15分钟 | Git, 文件系统 |
| 阶段2：开发脚本 | 2小时 | Python开发环境 |
| 阶段3：小样本测试 | 30分钟 | 测试环境 |
| 阶段4：批量处理 | 3-4小时 | 网络连接 |
| 阶段5：索引转换 | 30分钟 | 无 |
| 阶段6：验证报告 | 1小时 | 网络连接 |
| **总计** | **7-8小时** | |

### 资源需求
1. **计算资源**：
   - CPU：中等负载
   - 内存：~500MB（分批处理）
   - 磁盘：~100MB额外空间（备份）

2. **网络资源**：
   - 稳定网络连接（用于链接检查）
   - 预计网络请求：~3500次HEAD请求

3. **开发环境**：
   - Python 3.12+
   - Git
   - 文本编辑器

---

## 后续维护

### 监控机制
1. **定期链接检查**：每月检查一次外部链接有效性
2. **格式一致性检查**：新文档添加时自动格式化
3. **映射更新**：新命令添加时更新映射表

### 扩展性考虑
1. **支持新文档类型**：可扩展支持其他文档格式
2. **多语言支持**：可扩展支持中文文档优化
3. **自动化集成**：可与CI/CD流程集成

### 文档更新
1. **更新AGENTS.md**：记录优化脚本的使用方法
2. **更新README.md**：说明文档优化状态
3. **维护日志**：记录每次优化的详细情况

---

## 附录

### 附录A：特殊字符完整映射表
（完整的27个特殊字符映射表）

### 附录B：链接模式正则表达式
```python
# 完整的链接模式识别正则表达式
LINK_PATTERNS = {
    "command": re.compile(r"/hc/en-us/articles/(\d+)-([a-zA-Z0-9_-]+)"),
    "list_of_commands": re.compile(r"/hc/en-us/articles/360037228834"),
    "article": re.compile(r"/hc/en-us/articles/(\d+)-([A-Z][a-z]+[A-Za-z\s]*)"),
    "category": re.compile(r"/hc/en-us/categories/(\d+)"),
    "relative": re.compile(r"(\.\.?/[^)\s]+)"),
    "anchor": re.compile(r"#([a-zA-Z0-9_-]+)"),
}
```

### 附录C：验证检查清单
```markdown
## 优化后验证检查清单

### 链接验证
- [ ] 所有相对路径链接已转换为完整URL或本地链接
- [ ] 所有命令链接指向本地对应文档
- [ ] "List of commands"链接指向本地索引文件
- [ ] 所有外部链接通过HTTP HEAD验证

### 格式验证
- [ ] 所有文档通过mdformat格式化
- [ ] 表格格式正确无误
- [ ] 代码块格式正确
- [ ] 数学公式格式正确

### 映射验证
- [ ] 命令名↔文件名映射100%准确
- [ ] 索引文件表格格式正确
- [ ] 所有超链接可点击
```

---

## 版本历史
| 版本 | 日期 | 作者 | 描述 |
|------|------|------|------|
| 1.0 | 2026-02-08 | DeepSeek/Minimax | 初始版本，基于技术分析和review |
| 1.1 | 2026-02-08 |  | 根据用户反馈添加链接有效性检查要求 |

---

**状态**：待执行  
**优先级**：高  
**风险评估**：中（有完善的备份和回滚机制）  
**预计开始时间**：用户确认后立即执行