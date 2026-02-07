# Lumerical文档项目重组详细计划

## 📋 项目概述

### 当前状态
- **项目名称**：lumerical-docs (lumpy package)
- **主要工作内容**：
  1. AI手动整理高质量lumapi命令文档（已暂停）
  2. 从官网抓取LSF官方英文文档（已完成，727个命令）
  3. 将官方英文文档翻译成中文文档（进行中，手动翻译策略）

### 重组目标
1. **关注点分离**：三个工作内容独立到不同git分支
2. **代码优化**：整合重复功能，清理过时文件
3. **文档共享**：通用文档在各分支间保持一致
4. **功能完整性**：各分支具备完整的工作流程

### 分支结构
```
main (protected, default)
├── LSF英文文档抓取项目
├── 包含：抓取脚本 + 英文文档 + 共享文档
└── 未来可重命名为 `lumerical-lsf-scraper`

translation (feature branch)
├── 中文翻译工作分支
├── 包含：抓取脚本 + 翻译工具 + 中文文档 + 共享文档
└── 遵循手动翻译策略

lumapi (archive branch)
├── AI整理的Lumapi文档存档
├── 包含：Lumapi文档 + 最小共享文档
└── 不计划继续开发，仅作参考
```

## 🎯 核心原则

### 1. 共享依赖与环境
- **统一依赖管理**：所有分支共享相同的 `pyproject.toml` 和 `uv.lock`
- **环境一致性**：使用相同的Python 3.12+环境和开发工具
- **依赖精简**：保持当前依赖集，不拆分（main分支的依赖已满足所有需求）

### 2. 功能整合
- **翻译功能整合**：将多个翻译相关脚本整合为统一模块
- **抓取功能优化**：保留核心抓取脚本，移除临时/重复文件
- **质量工具统一**：整合质量评估和改进功能

### 3. 文档共享
- **通用文档共享**：AGENTS.md、开发指南等在分支间保持一致
- **分支特定文档**：各分支README明确说明分支用途和工作流程
- **历史记录保留**：通过分支创建保留所有文件历史

## 📋 详细执行计划

### 阶段0：准备工作（当前main分支）

#### 0.1 提交当前更改
```bash
# 查看当前状态
git status

# 添加并提交所有待提交的更改
git add .
git commit -m "chore: commit pending changes before reorganization (quality improvements, backup cleanup)"

# 验证提交
git log --oneline -5
```

#### 0.2 创建备份标签
```bash
# 创建备份标签
git tag pre-reorganization-$(date +%Y-%m-%d)

# 推送标签到远程
git push origin --tags

# 列出所有标签确认
git tag -l
```

#### 0.3 功能完整性验证
```bash
# 验证抓取功能
python scripts/scrape_one_command.py --list

# 验证翻译助手功能
python scripts/translation_helper.py --stats

# 运行代码质量检查
ruff check .
ruff format --check .

# 统计文档数量
echo "英文文档数量: $(find docs/lsf-script/en -name "*.md" | wc -l)"
echo "中文文档数量: $(find docs/lsf-script/cn -name "*.md" | wc -l)"
echo "Lumapi文档数量: $(find docs/lumapi -name "*.md" | wc -l)"
```

#### 0.4 创建计划文档目录
```bash
# 创建计划文档目录（已存在）
mkdir -p plan

# 记录初始状态
git rev-parse HEAD > plan/initial-commit.txt
git branch > plan/initial-branches.txt
```

### 阶段1：创建独立分支

#### 1.1 创建translation分支
```bash
# 从当前main创建translation分支
git checkout -b translation

# 推送到远程
git push -u origin translation

# 验证分支创建
git branch -a | grep translation
```

#### 1.2 创建lumapi分支
```bash
# 切换回main分支
git checkout main

# 创建lumapi分支
git checkout -b lumapi

# 推送到远程
git push -u origin lumapi

# 验证分支创建
git branch -a | grep lumapi
```

#### 1.3 分支结构验证
```bash
# 切换到main分支
git checkout main

# 验证各分支存在
echo "当前分支: $(git branch --show-current)"
echo "所有分支:"
git branch -a
```

### 阶段2：功能整合与清理

#### 2.1 翻译功能整合（在translation分支）
```bash
# 切换到translation分支
git checkout translation

# 分析翻译相关脚本
echo "=== 翻译相关脚本分析 ==="
ls scripts/*translate*.py scripts/*translation*.py scripts/*quality*.py 2>/dev/null

# 整合策略：
# 1. 保留核心工具
#   - translation_helper.py (主翻译助手)
#   - quality_assessment.py (质量评估)
# 2. 移除已放弃的批量翻译
#   - auto_translate.py, batch_translate.py, manual_batch_translate.py
#   - test_translate.py, section_scheduler.py
# 3. 保留辅助工具
#   - check_translation_status.py, find_untranslated.py (可考虑整合到translation_helper)
#   - generate_translation_report.py (可整合)
#   - restore_files.py (保留)

# 第一步：标记要移除的文件
cat > plan/translation-files-to-remove.txt << EOF
scripts/auto_translate.py
scripts/batch_translate.py
scripts/manual_batch_translate.py
scripts/test_translate.py
scripts/section_scheduler.py
scripts/generate_translation_report.py  # 功能已整合到translation_helper.py
EOF

# 第二步：整合功能到translation_helper.py
# 更新translation_helper.py，集成原generate_translation_report.py的功能
# 添加--integrated-report选项

# 第三步：更新check_translation_status.py和find_untranslated.py
# 优化功能，避免重复，或整合到translation_helper.py

# 第四步：移除文件
while read -r file; do
    if [ -f "$file" ]; then
        echo "移除: $file"
        rm "$file"
    fi
done < plan/translation-files-to-remove.txt

# 第五步：验证整合后功能
python scripts/translation_helper.py --help
python scripts/translation_helper.py --stats
python scripts/quality_assessment.py --help
```

#### 2.2 抓取功能优化（在main分支）
```bash
# 切换到main分支
git checkout main

# 分析抓取相关脚本
echo "=== 抓取相关脚本分析 ==="
ls scripts/*scrape*.py scripts/*update*.py scripts/*analyze*.py 2>/dev/null

# 整合策略：
# 1. 保留核心抓取工具
#   - scrape_one_command.py (单命令抓取)
#   - update_lsf_docs.py (批量更新)
#   - scrape_missing_lsf_docs.py (缺失命令抓取)
#   - update_lsf_docs_resume.py (断点续传)
#   - analyze_missing_commands.py (分析工具)
# 2. 优化功能
#   - batch_scrape_fast.py (可整合到update_lsf_docs.py)
# 3. 移除临时/测试文件
#   - temp_batch.sh, batch_scrape_10.sh
#   - sleep_script.py (限流功能可整合)
#   - test_fetch.py, test_selenium.py (测试文件保留)

# 第一步：标记要移除的临时文件
cat > plan/scraping-files-to-remove.txt << EOF
scripts/temp_batch.sh
scripts/batch_scrape_10.sh
scripts/sleep_script.py
scripts/manual_translate.py.backup
EOF

# 第二步：功能优化（可选）
# 将batch_scrape_fast.py的功能整合到update_lsf_docs.py
# 将sleep_script.py的限流功能整合到抓取函数中

# 第三步：移除临时文件
while read -r file; do
    if [ -f "$file" ]; then
        echo "移除: $file"
        rm "$file"
    fi
done < plan/scraping-files-to-remove.txt

# 第四步：验证抓取功能
python scripts/scrape_one_command.py --list
python scripts/update_lsf_docs.py --dry-run
```

#### 2.3 Lumapi分支最小化（在lumapi分支）
```bash
# 切换到lumapi分支
git checkout lumapi

# 清理策略：仅保留Lumapi文档和相关文档
# 移除所有脚本和无关文档

# 第一步：备份脚本目录结构（可选）
mkdir -p plan/backup
cp -r scripts plan/backup/scripts-backup/

# 第二步：清空scripts目录（保留目录结构）
rm -f scripts/*.py scripts/*.sh

# 第三步：创建最小工具集（可选）
# 如果需要，创建简单的文档查看工具
cat > scripts/README.md << 'EOF'
# Lumapi分支脚本目录

此分支为存档分支，不包含抓取或翻译脚本。

Lumapi文档位于: docs/lumapi/

如需开发工具，请切换到main或translation分支。
EOF

# 第四步：清理无关文档
rm -rf docs/lsf-script/
rm -f docs/translation-*.json
rm -f docs/batch_translation_log.json
rm -f docs/translation-workflow-guide.md
rm -f docs/translation-sections/
rm -f quality-report-50.json
rm -f quality-improvement-workflow.md

# 第五步：验证清理结果
echo "剩余文档:"
find docs/ -name "*.md" | wc -l
echo "剩余脚本:"
ls scripts/ 2>/dev/null || echo "scripts目录为空"
```

### 阶段3：文档共享与分支配置

#### 3.1 通用文档处理
```bash
# 通用文档列表（所有分支共享）
cat > plan/shared-documents.txt << EOF
README.md                   # 需要分支特定版本，但保留基本结构
AGENTS.md                   # AI代理指南，完全共享
pyproject.toml              # 依赖配置，完全共享
uv.lock                     # 锁文件，完全共享
.gitignore                  # Git忽略配置，完全共享
requirements.txt            # 备选依赖文件，完全共享
HISTORY.md                  # 项目历史，需要分支特定版本
LSF-DOCUMENTATION-SCRAPING-WORKFLOW.md  # 抓取工作流，main和translation共享
QUICK-START-SCRAPING.md     # 快速开始，main和translation共享
SCRAPING-PROJECT-COMPLETION-SUMMARY.md  # 项目总结，main和translation共享
EOF

# 文档共享策略：
# 1. 完全共享：AGENTS.md, pyproject.toml等
# 2. 分支特定：README.md, HISTORY.md需要分支定制
# 3. 条件共享：某些文档仅部分分支需要

# 创建文档同步脚本
cat > plan/sync-shared-docs.sh << 'EOF'
#!/bin/bash
# 同步共享文档到指定分支

BRANCH=$1
SHARED_FILES="AGENTS.md pyproject.toml uv.lock .gitignore requirements.txt"

if [ -z "$BRANCH" ]; then
    echo "用法: $0 <branch-name>"
    exit 1
fi

# 切换到目标分支
git checkout $BRANCH

# 同步每个共享文件
for file in $SHARED_FILES; do
    if [ -f "../$file" ]; then
        cp "../$file" "$file"
        echo "已同步: $file"
    fi
done

echo "共享文档同步完成到分支: $BRANCH"
EOF

chmod +x plan/sync-shared-docs.sh
```

#### 3.2 分支特定README更新

**main分支README模板:**
```markdown
# Lumerical LSF Script Documentation Scraper

## 项目概述
专注于从Ansys Optics知识库抓取Lumerical Scripting Language (LSF)命令文档，生成本地可搜索的Markdown仓库。

## 当前状态
- **总命令数**: 727
- **已抓取**: 727个命令（100%完成）
- **文档位置**: `docs/lsf-script/en/`

## 快速开始
```bash
# 查看可用命令
python scripts/scrape_one_command.py --list

# 抓取单个命令
python scripts/scrape_one_command.py "addmaterial"

# 批量更新
python scripts/update_lsf_docs.py
```

## 分支结构
- `main`: LSF英文文档抓取（本分支）
- `translation`: 中文翻译工作分支
- `lumapi`: Lumapi文档存档分支
```

**translation分支README模板:**
```markdown
# Lumerical LSF文档中文翻译

## 项目概述
将LSF官方英文文档翻译为中文，遵循**手动逐条翻译**策略，确保翻译质量。

## 当前进度
- **总命令数**: 727
- **已翻译**: [数量]个命令 ([进度]%)
- **翻译策略**: 手动逐条翻译，质量优先

## 翻译工具
```bash
# 查看翻译进度
python scripts/translation_helper.py --stats

# 列出未翻译命令
python scripts/translation_helper.py --list

# 准备翻译模板
python scripts/translation_helper.py --prepare addmaterial
```

## 质量保证
- 使用 `quality_assessment.py` 进行质量评估
- 手动审核所有翻译
- 定期生成质量报告
```

**lumapi分支README模板:**
```markdown
# Lumapi Python API文档（存档）

## 项目概述
AI手动整理的Lumapi Python API命令文档存档。**此分支已暂停开发**，仅作为参考文档。

## 文档状态
- **总命令数**: 86个已整理命令
- **开发状态**: 已暂停
- **文档质量**: 手动整理，包含详细说明和示例

## 分支说明
- 此分支为存档分支，不计划继续开发
- 如需抓取或翻译功能，请切换到 `main` 或 `translation` 分支
- 文档位置: `docs/lumapi/`
```

#### 3.3 更新HISTORY.md
```bash
# 在各分支更新HISTORY.md，添加重组记录

# main分支版本
cat >> HISTORY.md << 'EOF'

## 项目重组 (2026-02-07)

### 重组决策
基于项目发展现状，决定将三个主要工作内容分离到独立git分支：
1. **main分支**: 专注于LSF英文文档抓取（已完成727个命令）
2. **translation分支**: 中文翻译工作（遵循手动翻译策略）
3. **lumapi分支**: AI整理的Lumapi文档存档（工作已暂停）

### 重组执行
- 清理过时文件（备份、临时文件）
- 整合重复功能脚本
- 共享通用文档（AGENTS.md, 开发指南等）
- 各分支保持独立工作流程

### 下一步
- 完善LSF英文文档质量
- 推进中文手动翻译
- 维护分支间文档同步
EOF

# translation分支类似更新
# lumapi分支类似更新
```

### 阶段4：验证与测试

#### 4.1 各分支功能验证
```bash
# 验证脚本：plan/verify-branches.sh
cat > plan/verify-branches.sh << 'EOF'
#!/bin/bash
echo "=== 分支重组验证测试 ==="

# 测试main分支
echo "1. 测试main分支..."
git checkout main
echo "当前分支: $(git branch --show-current)"
python scripts/scrape_one_command.py --list > /dev/null && echo "✅ 抓取功能正常"
ruff check . > /dev/null 2>&1 && echo "✅ 代码检查通过"
echo "文档数量: $(find docs/lsf-script/en -name '*.md' 2>/dev/null | wc -l)"

# 测试translation分支
echo -e "\n2. 测试translation分支..."
git checkout translation
echo "当前分支: $(git branch --show-current)"
python scripts/translation_helper.py --stats > /dev/null && echo "✅ 翻译助手正常"
[ -f scripts/quality_assessment.py ] && echo "✅ 质量工具存在"
echo "中文文档: $(find docs/lsf-script/cn -name '*.md' 2>/dev/null | wc -l)"

# 测试lumapi分支
echo -e "\n3. 测试lumapi分支..."
git checkout lumapi
echo "当前分支: $(git branch --show-current)"
[ -d docs/lumapi ] && echo "✅ Lumapi文档存在"
echo "Lumapi文档: $(find docs/lumapi -name '*.md' 2>/dev/null | wc -l)"
[ ! -f scripts/scrape_one_command.py ] && echo "✅ 抓取脚本已清理"

echo -e "\n=== 验证完成 ==="
EOF

chmod +x plan/verify-branches.sh

# 运行验证
./plan/verify-branches.sh
```

#### 4.2 依赖与环境验证
```bash
# 验证各分支依赖一致性
cat > plan/verify-dependencies.sh << 'EOF'
#!/bin/bash
echo "=== 依赖一致性验证 ==="

# 检查各分支的pyproject.toml
for branch in main translation lumapi; do
    echo -e "\n检查分支: $branch"
    git checkout $branch > /dev/null 2>&1
    
    if [ -f pyproject.toml ]; then
        echo "✅ pyproject.toml 存在"
        # 检查关键依赖
        grep -q "beautifulsoup4" pyproject.toml && echo "✅ 包含BeautifulSoup4"
        grep -q "selenium" pyproject.toml && echo "✅ 包含Selenium"
    else
        echo "❌ pyproject.toml 缺失"
    fi
done

# 返回main分支
git checkout main > /dev/null 2>&1
echo -e "\n=== 依赖验证完成 ==="
EOF

chmod +x plan/verify-dependencies.sh
./plan/verify-dependencies.sh
```

#### 4.3 文档完整性验证
```bash
# 验证文档完整性
cat > plan/verify-documents.sh << 'EOF'
#!/bin/bash
echo "=== 文档完整性验证 ==="

echo "1. 共享文档检查:"
for doc in AGENTS.md pyproject.toml .gitignore; do
    if [ -f "$doc" ]; then
        echo "✅ $doc 存在"
    else
        echo "❌ $doc 缺失"
    fi
done

echo -e "\n2. 各分支特定文档:"
git checkout main && echo "main README: $(head -5 README.md | grep -c 'LSF')/5"
git checkout translation && echo "translation README: $(head -5 README.md | grep -c '翻译')/5"
git checkout lumapi && echo "lumapi README: $(head -5 README.md | grep -c '存档')/5"

git checkout main
echo -e "\n=== 文档验证完成 ==="
EOF

chmod +x plan/verify-documents.sh
./plan/verify-documents.sh
```

### 阶段5：提交与同步

#### 5.1 提交各分支更改
```bash
# 提交main分支更改
git checkout main
git add .
git commit -m "refactor: reorganize project structure - main branch (LSF scraping only)"
git push origin main

# 提交translation分支更改
git checkout translation
git add .
git commit -m "refactor: reorganize project structure - translation branch (manual translation workflow)"
git push origin translation

# 提交lumapi分支更改
git checkout lumapi
git add .
git commit -m "refactor: reorganize project structure - lumapi branch (archive only)"
git push origin lumapi
```

#### 5.2 创建重组完成标签
```bash
# 切换到main分支
git checkout main

# 创建完成标签
git tag post-reorganization-$(date +%Y-%m-%d)

# 推送到所有分支（可选）
git push origin --tags

# 标签列表
echo "重组前后标签:"
git tag -l | grep reorganization
```

#### 5.3 生成重组报告
```bash
# 生成重组报告
cat > plan/reorganization-report.md << EOF
# 项目重组完成报告

## 执行时间
$(date)

## 分支状态
| 分支 | 文档数量 | 脚本数量 | 状态 |
|------|----------|----------|------|
| main | $(find docs/lsf-script/en -name "*.md" 2>/dev/null | wc -l) | $(ls scripts/*.py 2>/dev/null | wc -l) | ✅ 正常 |
| translation | $(find docs/lsf-script/cn -name "*.md" 2>/dev/null | wc -l) | $(ls scripts/*.py 2>/dev/null | wc -l) | ✅ 正常 |
| lumapi | $(find docs/lumapi -name "*.md" 2>/dev/null | wc -l) | $(ls scripts/*.py 2>/dev/null | wc -l) | ✅ 存档 |

## 文件变更统计
- **移除文件**: $(wc -l < plan/translation-files-to-remove.txt)+$(wc -l < plan/scraping-files-to-remove.txt) 个
- **整合脚本**: 翻译功能整合到 translation_helper.py
- **共享文档**: $(wc -l < plan/shared-documents.txt) 个文件在各分支间共享

## 验证结果
$(./plan/verify-branches.sh 2>&1 | sed 's/^/    /')

## 后续建议
1. 定期运行文档同步脚本保持共享文档一致
2. 在translation分支推进手动翻译工作
3. 考虑将main分支重命名为更准确的项目名
4. 建立分支合并和同步流程

## 风险与回滚
如需回滚到重组前状态:
\`\`\`bash
git checkout pre-reorganization-YYYY-MM-DD
\`\`\`
EOF

echo "重组报告已生成: plan/reorganization-report.md"
```

## 🛡️ 风险管理

### 风险矩阵
| 风险 | 概率 | 影响 | 缓解措施 |
|------|------|------|----------|
| 数据丢失 | 低 | 高 | 创建pre-reorganization标签，提供完整回滚方案 |
| 功能破坏 | 中 | 中 | 各阶段独立验证，确保核心功能正常 |
| 依赖冲突 | 低 | 低 | 保持共享依赖，不拆分pyproject.toml |
| 协作混乱 | 中 | 中 | 明确文档说明各分支用途和工作流程 |
| Git操作错误 | 低 | 中 | 分阶段执行，每阶段验证后才继续 |

### 回滚方案
```bash
# 完全回滚到重组前
git checkout pre-reorganization-YYYY-MM-DD
git checkout -b main-recovered
git push -u origin main-recovered

# 部分回滚（某分支）
git checkout translation
git reset --hard origin/translation@{1}
git push --force origin translation
```

### 应急联系人
- 问题：Git操作失误 -> 参考回滚方案
- 问题：功能异常 -> 切换回标签版本测试
- 问题：文档不一致 -> 运行sync-shared-docs.sh

## 📊 交付物清单

### 文档交付物
1. `plan/project-reorganization-detailed.md` - 本详细计划
2. `plan/reorganization-report.md` - 重组完成报告
3. `plan/file-classification-matrix.csv` - 文件分类矩阵
4. `plan/branch-specification.md` - 分支规范说明

### 脚本交付物
1. `plan/verify-branches.sh` - 分支验证脚本
2. `plan/verify-dependencies.sh` - 依赖验证脚本  
3. `plan/verify-documents.sh` - 文档验证脚本
4. `plan/sync-shared-docs.sh` - 文档同步脚本

### Git交付物
1. 三个功能独立的分支：`main`, `translation`, `lumapi`
2. 两个标签：`pre-reorganization`, `post-reorganization`
3. 完整的提交历史，包含重组记录

## 📅 执行时间线

| 阶段 | 预计耗时 | 关键产出 | 负责人 |
|------|----------|----------|--------|
| 阶段0：准备 | 30分钟 | 备份标签，初始验证 | AI代理 |
| 阶段1：创建分支 | 15分钟 | 三个独立分支 | AI代理 |
| 阶段2：功能整合 | 60分钟 | 整合后代码，清理文件 | AI代理 |
| 阶段3：文档配置 | 45分钟 | 分支特定README，共享文档 | AI代理 |
| 阶段4：验证测试 | 30分钟 | 验证报告，问题修复 | AI代理 |
| 阶段5：提交同步 | 20分钟 | 提交记录，最终标签 | AI代理 |
| **总计** | **3小时** | **完整重组项目** | **AI代理** |

## ✅ 成功标准

### 技术标准
1. ✅ 三个分支独立创建并推送
2. ✅ 各分支核心功能正常运行
3. ✅ 代码通过ruff检查，无语法错误
4. ✅ 文档数量统计正确（英文727，中文...，lumapi 86）
5. ✅ 共享文档在各分支一致

### 项目标准
1. ✅ 关注点分离达成：各分支专注于特定工作
2. ✅ 代码优化完成：重复功能整合，临时文件清理
3. ✅ 文档完整性：分支说明清晰，历史记录完整
4. ✅ 可维护性：各分支具备独立工作流程
5. ✅ 可扩展性：支持未来项目发展和分支策略调整

## 🔄 后续维护

### 定期同步
```bash
# 每月运行一次文档同步
./plan/sync-shared-docs.sh main
./plan/sync-shared-docs.sh translation  
./plan/sync-shared-docs.sh lumapi
```

### 分支更新策略
- **main分支**：默认分支，受保护，需PR审核
- **translation分支**：特性分支，可直接推送，定期从main拉取更新
- **lumapi分支**：存档分支，只读，不计划更新

### 质量保证
- 每次重要变更后运行验证脚本
- 定期生成项目状态报告
- 保持文档和代码一致性

---

**批准执行**：待用户审阅确认后，按此计划执行项目重组。

**审阅要点**：
1. 分支策略是否符合需求
2. 功能整合方案是否合理
3. 风险控制措施是否充分
4. 执行时间线是否可行

请提供反馈意见，确认后开始执行。