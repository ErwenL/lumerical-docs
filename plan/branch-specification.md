# 分支规范与协作指南

## 分支概述

### 分支结构图
```
main (protected, default)
├── 用途: LSF英文文档抓取项目
├── 状态: 活跃开发，文档抓取已完成
├── 保护: 需要PR审核
└── 同步: 定期同步到特性分支

translation (feature branch)
├── 用途: 中文文档翻译工作
├── 状态: 活跃开发，手动翻译进行中
├── 保护: 可直接推送
└── 同步: 从main定期拉取更新

lumapi (archive branch)
├── 用途: AI整理的Lumapi文档存档
├── 状态: 已暂停，只读存档
├── 保护: 只读，不计划更新
└── 同步: 不主动同步
```

## 分支详细规范

### 1. main分支

#### 1.1 分支定义
- **名称**: `main` (默认分支)
- **别名**: `master` (已弃用)
- **目标**: LSF英文文档抓取项目的稳定版本
- **状态**: 受保护，仅接受经过测试的更改

#### 1.2 内容范围
```
main/
├── docs/lsf-script/en/          # 英文文档 (727个命令)
├── scripts/                     # 抓取脚本
│   ├── scrape_one_command.py
│   ├── update_lsf_docs.py
│   ├── scrape_missing_lsf_docs.py
│   ├── update_lsf_docs_resume.py
│   ├── analyze_missing_commands.py
│   └── batch_scrape_fast.py
├── docs/                        # 项目文档
│   ├── script-commands-alphabetical.md
│   ├── script-commands-by-category.md
│   ├── missing-lsf-script-docs.md
│   └── 其他抓取相关文档
└── 共享配置文件
    ├── pyproject.toml
    ├── AGENTS.md
    └── 其他共享文件
```

#### 1.3 开发规则
1. **分支策略**: Git Flow简化版
   - `main` 分支保持稳定
   - 新功能在特性分支开发
   - 通过PR合并到main

2. **提交规范**:
   ```
   feat: 添加新功能
   fix: 修复bug
   docs: 文档更新
   refactor: 代码重构
   test: 测试相关
   chore: 维护任务
   ```

3. **PR要求**:
   - 描述清晰的PR标题和说明
   - 关联issue（如有）
   - 通过CI/CD检查
   - 至少一个代码审查
   - 更新相关文档

#### 1.4 保护规则
```yaml
# GitHub分支保护规则建议
protected: true
required_status_checks:
  strict: true
  contexts:
    - "ci/cd"
    - "lint"
required_pull_request_reviews:
  required_approving_review_count: 1
  dismiss_stale_reviews: true
restrictions: null  # 允许特定用户推送
allow_force_pushes: false
allow_deletions: false
```

### 2. translation分支

#### 2.1 分支定义
- **名称**: `translation`
- **类型**: 特性分支 (long-lived feature branch)
- **目标**: 中文文档翻译工作
- **状态**: 活跃开发，手动翻译策略

#### 2.2 内容范围
```
translation/
├── 继承main分支所有内容
├── docs/lsf-script/cn/          # 中文翻译文档
├── scripts/                     # 翻译相关脚本
│   ├── translation_helper.py    # 主翻译工具
│   ├── quality_assessment.py    # 质量评估
│   ├── check_translation_status.py
│   ├── find_untranslated.py
│   └── restore_files.py
├── docs/                        # 翻译相关文档
│   ├── translation-progress.json
│   ├── translation-workflow-guide.md
│   └── 其他翻译文档
└── 共享配置文件 (与main相同)
```

#### 2.3 工作流程
1. **翻译流程**:
   ```
   1. 使用翻译助手列出未翻译命令
      python scripts/translation_helper.py --list
      
   2. 准备翻译模板
      python scripts/translation_helper.py --prepare <command>
      
   3. 手动编辑中文文档
      vim docs/lsf-script/cn/<command>.md
      
   4. 质量评估
      python scripts/quality_assessment.py <command>
      
   5. 更新进度
      python scripts/translation_helper.py --stats
   ```

2. **分支同步**:
   ```bash
   # 从main分支获取最新抓取功能
   git fetch origin main
   git merge origin/main --no-ff
   
   # 解决合并冲突（如有）
   # 保持翻译相关文件不变
   ```

3. **提交策略**:
   - 可直接推送到translation分支
   - 建议小步提交，每次翻译1-3个命令
   - 提交信息包含翻译的命令名称

#### 2.4 质量保证
1. **翻译质量标准**:
   - 准确性：术语翻译准确
   - 一致性：相同术语统一翻译
   - 可读性：中文表达自然流畅
   - 完整性：不遗漏重要信息

2. **质量检查**:
   ```bash
   # 运行质量评估
   python scripts/quality_assessment.py --all
   
   # 生成质量报告
   python scripts/translation_helper.py --report
   ```

### 3. lumapi分支

#### 3.1 分支定义
- **名称**: `lumapi`
- **类型**: 存档分支 (archive branch)
- **目标**: AI整理的Lumapi文档存档
- **状态**: 已暂停，只读参考

#### 3.2 内容范围
```
lumapi/
├── docs/lumapi/                 # Lumapi文档 (86个命令)
├── docs/lumapi-principles.md    # Lumapi原理文档
├── scripts/README.md            # 脚本目录说明
└── 最小共享配置文件
    ├── pyproject.toml          # （可选，可精简）
    └── .gitignore
```

#### 3.3 管理规则
1. **只读原则**:
   - 不计划新功能开发
   - 不修复bug（除非严重错误）
   - 不接受新文档添加

2. **存档目的**:
   - 历史参考：记录已完成的AI整理工作
   - 文档查询：作为Lumapi API的参考文档
   - 项目完整性：保留项目历史的一部分

3. **维护策略**:
   - 定期安全更新（依赖漏洞修复）
   - 文档格式修正（如Markdown格式）
   - 不进行内容更新或功能添加

## 分支协作流程

### 跨分支同步

#### 从main同步到translation
```bash
# 在translation分支执行
git checkout translation
git fetch origin main
git merge origin/main --no-ff -m "chore: sync from main $(date +%Y-%m-%d)"

# 解决可能的冲突
# - 抓取脚本更新：接受main版本
# - 翻译相关文件：保留translation版本
# - 共享文档：根据情况决定
```

#### 从main同步到lumapi（可选）
```bash
# 在lumapi分支执行（仅共享配置更新）
git checkout lumapi
git fetch origin main
# 选择性合并共享配置
git checkout origin/main -- pyproject.toml AGENTS.md .gitignore
git commit -m "chore: update shared config from main"
```

### 分支间代码共享

#### 共享配置管理
1. **完全共享文件** (自动同步):
   ```
   pyproject.toml
   uv.lock
   AGENTS.md
   .gitignore
   requirements.txt
   ```

2. **分支特定文件** (手动管理):
   ```
   README.md          # 各分支不同
   HISTORY.md         # 各分支不同  
   docs/目录内容      # 各分支不同
   ```

3. **同步脚本**:
   ```bash
   # 运行同步脚本（在plan/目录）
   ./plan/sync-shared-docs.sh <branch-name>
   ```

#### 功能开发协作
1. **抓取功能改进**:
   - 在main分支开发
   - 测试通过后合并到main
   - translation分支通过同步获取更新

2. **翻译工具改进**:
   - 在translation分支开发
   - 如果通用性高，可考虑回馈到main
   - 通过PR从translation合并到main

3. **文档更新**:
   - 各分支独立维护文档
   - 通用文档更新需同步到所有分支

### 冲突解决指南

#### 常见冲突场景
1. **共享配置冲突**:
   ```
   冲突文件: pyproject.toml
   解决方案: 讨论决定哪个版本更合适
             或创建兼容两个分支的版本
   ```

2. **脚本功能冲突**:
   ```
   冲突文件: scripts/scrape_one_command.py
   解决方案: main分支的版本优先
             因为main是抓取功能的权威分支
   ```

3. **文档内容冲突**:
   ```
   冲突文件: docs/lsf-script/en/addmaterial.md
   解决方案: main分支的版本优先
             英文文档以main为准
   ```

#### 冲突解决流程
```bash
# 1. 识别冲突
git status
# 显示冲突文件

# 2. 手动解决冲突
# 编辑冲突文件，保留需要的更改
# 删除冲突标记 <<<<<<<, =======, >>>>>>>

# 3. 标记解决
git add <resolved-file>

# 4. 完成合并
git commit
```

## 分支权限与访问控制

### 开发团队角色
| 角色 | main分支 | translation分支 | lumapi分支 | 职责 |
|------|----------|----------------|------------|------|
| **维护者** | ✅ 直接推送 | ✅ 直接推送 | ✅ 直接推送 | 项目管理，冲突解决 |
| **抓取开发者** | ✅ PR合并 | ✅ 只读访问 | ✅ 只读访问 | 抓取功能开发 |
| **翻译贡献者** | ✅ 只读访问 | ✅ 直接推送 | ✅ 只读访问 | 文档翻译工作 |
| **文档查阅者** | ✅ 只读访问 | ✅ 只读访问 | ✅ 只读访问 | 文档使用和参考 |

### 权限矩阵
| 操作 | main | translation | lumapi |
|------|------|-------------|--------|
| 创建PR | ✅ | ✅ (可选) | ❌ |
| 合并PR | ✅ (需审核) | ✅ (可选) | ❌ |
| 直接推送 | ⚠️ (维护者) | ✅ | ⚠️ (仅维护) |
| 创建分支 | ✅ | ✅ | ❌ |
| 删除分支 | ⚠️ (维护者) | ⚠️ (维护者) | ⚠️ (维护者) |
| 标签操作 | ✅ | ✅ | ❌ |

## 分支生命周期管理

### 分支创建
1. **main分支**: 初始分支，永久存在
2. **translation分支**: 从main创建，长期存在
3. **lumapi分支**: 从main创建，永久存档

### 分支更新频率
| 分支 | 更新频率 | 更新内容 | 更新方式 |
|------|----------|----------|----------|
| main | 按需 | 抓取功能改进，文档更新 | PR合并 |
| translation | 每周 | 翻译进度更新，质量改进 | 直接推送 |
| lumapi | 极少 | 安全更新，格式修正 | 维护者操作 |

### 分支合并策略
1. **main分支合并**:
   - Squash and Merge（推荐）
   - 保持提交历史整洁
   - 便于问题追踪

2. **跨分支同步**:
   - Merge Commit（保留历史）
   - 明确同步来源和时间

### 分支清理规则
1. **临时分支**: 功能完成后删除
2. **特性分支**: 长期特性可保留
3. **存档分支**: 永久保留，不删除

## 开发环境配置

### 多分支工作流
```bash
# 克隆项目
git clone <repository-url>
cd lumerical-docs

# 查看所有分支
git branch -a

# 切换分支
git checkout main          # LSF抓取工作
git checkout translation   # 翻译工作
git checkout lumapi       # 文档查阅

# 创建新特性分支（从main）
git checkout main
git checkout -b feature/new-scraping-method
```

### 依赖管理
```bash
# 所有分支使用相同依赖
uv sync

# 验证环境
python -c "import cloudscraper, bs4; print('依赖正常')"
```

### 开发工具配置
1. **预提交钩子** (推荐):
   ```yaml
   # .pre-commit-config.yaml
   repos:
     - repo: https://github.com/astral-sh/ruff-pre-commit
       rev: v0.1.0
       hooks:
         - id: ruff
           args: [--fix]
         - id: ruff-format
   ```

2. **编辑器配置**:
   - VS Code: Python扩展，Markdown扩展
   - 代码格式化: 使用Ruff
   - 编码规范: 遵循AGENTS.md指南

## 监控与维护

### 分支健康检查
1. **定期检查项**:
   ```bash
   # 运行验证脚本
   ./plan/verify-branches.sh
   
   # 检查分支同步状态
   git log --oneline main..translation  # translation超前提交
   git log --oneline translation..main  # main超前提交
   ```

2. **质量指标**:
   - main分支: 抓取成功率，文档完整性
   - translation分支: 翻译进度，翻译质量评分
   - lumapi分支: 文档可访问性

### 问题处理流程
1. **发现问题**:
   - 运行验证脚本失败
   - 功能测试失败
   - 用户报告问题

2. **问题分类**:
   - 抓取问题 → main分支处理
   - 翻译问题 → translation分支处理
   - 文档问题 → 相应分支处理

3. **修复流程**:
   ```bash
   # 1. 创建修复分支
   git checkout <affected-branch>
   git checkout -b fix/<issue-description>
   
   # 2. 修复问题
   # 编辑代码，修复问题
   
   # 3. 测试验证
   ./plan/verify-branches.sh
   
   # 4. 提交修复
   git add .
   git commit -m "fix: <issue-description>"
   
   # 5. 合并修复
   # main分支: 通过PR
   # translation分支: 直接推送或PR
   # lumapi分支: 维护者操作
   ```

## 附录

### 常用命令参考
```bash
# 分支操作
git branch -a                    # 查看所有分支
git checkout <branch>           # 切换分支
git checkout -b <new-branch>    # 创建并切换分支

# 同步操作
git fetch origin --all          # 获取所有远程分支
git merge origin/main           # 合并main分支更新
git rebase origin/main          # 变基到main分支

# 状态检查
git status                     # 查看状态
git log --oneline --graph     # 查看提交历史
git diff main..translation    # 比较分支差异

# 清理操作
git branch -d <branch>        # 删除本地分支
git push origin --delete <branch>  # 删除远程分支
git fetch --prune             # 清理已删除的远程分支引用
```

### 联系与支持
- **问题报告**: GitHub Issues
- **讨论交流**: GitHub Discussions
- **紧急问题**: 项目维护者

### 文档更新记录
| 日期 | 版本 | 更新内容 | 更新人 |
|------|------|----------|--------|
| 2026-02-07 | 1.0 | 初始版本，项目重组规范 | AI代理 |
| 2026-02-07 | 1.1 | 添加详细工作流程和权限矩阵 | AI代理 |

---

**生效日期**: 2026-02-07  
**审查周期**: 每季度审查更新  
**负责团队**: 项目维护者  
**文档状态**: 正式生效