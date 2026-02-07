# 文件分类矩阵

## 分类说明
- **Lumapi**：AI手动整理的Lumapi文档（已暂停）
- **Scraping**：LSF英文文档抓取（已完成）
- **Translation**：中文文档翻译（进行中）
- **Shared**：各分支共享文件
- **Obsolete**：过时/临时文件（建议删除）

## 核心文件分类

### 根目录文件
| 文件 | 分类 | Main分支 | Translation分支 | Lumapi分支 | 备注 |
|------|------|----------|----------------|------------|------|
| `README.md` | Shared* | ✅ 定制版 | ✅ 定制版 | ✅ 定制版 | 各分支需要特定版本 |
| `HISTORY.md` | Shared* | ✅ 定制版 | ✅ 定制版 | ✅ 定制版 | 各分支记录不同历史 |
| `AGENTS.md` | Shared | ✅ 保留 | ✅ 保留 | ✅ 保留 | AI代理指南，完全共享 |
| `pyproject.toml` | Shared | ✅ 保留 | ✅ 保留 | ✅ 保留 | 依赖管理，完全共享 |
| `uv.lock` | Shared | ✅ 保留 | ✅ 保留 | ✅ 保留 | 锁文件，完全共享 |
| `.gitignore` | Shared | ✅ 保留 | ✅ 保留 | ✅ 保留 | Git忽略配置，完全共享 |
| `requirements.txt` | Shared | ✅ 保留 | ✅ 保留 | ✅ 保留 | 备选依赖文件，完全共享 |
| `LSF-DOCUMENTATION-SCRAPING-WORKFLOW.md` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 抓取工作流，translation需要 |
| `QUICK-START-SCRAPING.md` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 快速开始，translation需要 |
| `SCRAPING-PROJECT-COMPLETION-SUMARRY.md` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 项目总结，translation需要 |
| `quality-report-50.json` | Translation | ❌ 移除 | ✅ 保留 | ❌ 移除 | 翻译质量报告 |
| `quality-improvement-workflow.md` | Translation | ❌ 移除 | ✅ 保留 | ❌ 移除 | 质量改进工作流 |

### 脚本文件 (`scripts/`)
| 文件 | 分类 | Main分支 | Translation分支 | Lumapi分支 | 功能说明 |
|------|------|----------|----------------|------------|----------|
| `scrape_one_command.py` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 单命令抓取 |
| `update_lsf_docs.py` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 批量更新 |
| `scrape_missing_lsf_docs.py` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 缺失命令抓取 |
| `update_lsf_docs_resume.py` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 断点续传 |
| `analyze_missing_commands.py` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 分析工具 |
| `batch_scrape_fast.py` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 快速批量抓取 |
| `test_fetch.py` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 抓取测试 |
| `test_selenium.py` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | Selenium测试 |
| `setup_scraping_env.py` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 环境设置 |
| `translation_helper.py` | Translation | ❌ 移除 | ✅ 保留 | ❌ 移除 | 主翻译助手 |
| `quality_assessment.py` | Translation | ❌ 移除 | ✅ 保留 | ❌ 移除 | 质量评估工具 |
| `quality_improvement.py` | Translation | ❌ 移除 | ✅ 保留 | ❌ 移除 | 质量改进工具 |
| `check_translation_status.py` | Translation | ❌ 移除 | ✅ 保留 | ❌ 移除 | 翻译状态检查 |
| `find_untranslated.py` | Translation | ❌ 移除 | ✅ 保留 | ❌ 移除 | 查找未翻译 |
| `restore_files.py` | Translation | ❌ 移除 | ✅ 保留 | ❌ 移除 | 文件恢复工具 |
| `auto_translate.py` | Translation* | ❌ 移除 | ❌ 移除 | ❌ 移除 | **批量翻译（已放弃）** |
| `batch_translate.py` | Translation* | ❌ 移除 | ❌ 移除 | ❌ 移除 | **批量翻译（已放弃）** |
| `manual_batch_translate.py` | Translation* | ❌ 移除 | ❌ 移除 | ❌ 移除 | **批量翻译（已放弃）** |
| `test_translate.py` | Translation* | ❌ 移除 | ❌ 移除 | ❌ 移除 | **翻译测试（已放弃）** |
| `section_scheduler.py` | Translation* | ❌ 移除 | ❌ 移除 | ❌ 移除 | **分区调度（已放弃）** |
| `generate_translation_report.py` | Translation* | ❌ 移除 | ❌ 移除 | ❌ 移除 | **功能已整合** |
| `sleep_script.py` | Obsolete | ❌ 移除 | ❌ 移除 | ❌ 移除 | 限流脚本（可整合） |
| `temp_batch.sh` | Obsolete | ❌ 移除 | ❌ 移除 | ❌ 移除 | 临时脚本 |
| `batch_scrape_10.sh` | Obsolete | ❌ 移除 | ❌ 移除 | ❌ 移除 | 临时脚本 |
| `manual_translate.py.backup` | Obsolete | ❌ 移除 | ❌ 移除 | ❌ 移除 | 备份文件 |

### 文档文件 (`docs/`)
| 目录/文件 | 分类 | Main分支 | Translation分支 | Lumapi分支 | 说明 |
|----------|------|----------|----------------|------------|------|
| `lsf-script/en/` | Scraping | ✅ 保留（727文件） | ✅ 保留（727文件） | ❌ 移除 | 英文文档核心 |
| `lsf-script/cn/` | Translation | ❌ 移除 | ✅ 保留（部分文件） | ❌ 移除 | 中文翻译文档 |
| `lumapi/` | Lumapi | ❌ 移除 | ❌ 移除 | ✅ 保留（86文件） | Lumapi文档 |
| `lumapi-principles.md` | Lumapi | ❌ 移除 | ❌ 移除 | ✅ 保留 | Lumapi原理文档 |
| `translation-progress.json` | Translation | ❌ 移除 | ✅ 保留 | ❌ 移除 | 翻译进度 |
| `translation-progress-detailed.json` | Translation | ❌ 移除 | ✅ 保留 | ❌ 移除 | 详细进度 |
| `translation-report.json` | Translation | ❌ 移除 | ✅ 保留 | ❌ 移除 | 翻译报告 |
| `batch_translation_log.json` | Translation | ❌ 移除 | ✅ 保留 | ❌ 移除 | 批量翻译日志 |
| `translation-workflow-guide.md` | Translation | ❌ 移除 | ✅ 保留 | ❌ 移除 | 翻译工作流指南 |
| `translation-sections/` | Translation* | ❌ 移除 | ❌ 移除 | ❌ 移除 | **翻译分区（已放弃）** |
| `documentation-quality-standards.md` | Shared* | ✅ 保留 | ✅ 保留 | ❌ 移除 | 质量标准 |
| `DOCUMENTATION-TASK-SPEC.md` | Shared* | ✅ 保留 | ✅ 保留 | ❌ 移除 | 任务规范 |
| `script-commands-alphabetical.md` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 字母序命令列表 |
| `script-commands-by-category.md` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 分类命令列表 |
| `missing-lsf-script-docs.md` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 缺失命令文档 |
| `verification-result.md` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 验证结果 |
| `completeness-validation.md` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 完整性验证 |
| `INCREMENTAL-SCRAPING-GUIDE.md` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | 增量抓取指南 |
| `lsf-script-commands-alphabetical.md` | Scraping | ✅ 保留 | ✅ 保留 | ❌ 移除 | LSF命令字母序 |

## 文件统计

### 重组前统计
- **总文件数**: ~1500+个文件
- **英文文档**: 727个 `.md` 文件
- **中文文档**: 730个 `.md` 文件（部分为模板）
- **Lumapi文档**: 86个 `.md` 文件
- **Python脚本**: 23个 `.py` 文件
- **Shell脚本**: 3个 `.sh` 文件
- **配置文件**: 8个文件

### 重组后各分支目标
| 分支 | 英文文档 | 中文文档 | Lumapi文档 | 脚本文件 | 总文件数 |
|------|----------|----------|-------------|----------|----------|
| **main** | 727 | 0 | 0 | ~10 | ~750 |
| **translation** | 727 | 部分 | 0 | ~8 | ~750+ |
| **lumapi** | 0 | 0 | 86 | 0-2 | ~90 |

## 功能整合建议

### 翻译功能整合
**当前问题**: 多个翻译相关脚本功能重叠
**整合方案**:
```
translation_helper.py (核心)
├── 原有功能
├── 整合 generate_translation_report.py 的报告功能
├── 整合 check_translation_status.py 的状态检查
└── 整合 find_untranslated.py 的查找功能

quality_assessment.py (质量评估)
├── 原有功能
└── 整合 quality_improvement.py 的改进建议

删除: auto_translate.py, batch_translate.py, manual_batch_translate.py, test_translate.py, section_scheduler.py
```

### 抓取功能优化
**当前问题**: 存在临时文件和测试脚本
**优化方案**:
```
保留核心:
- scrape_one_command.py
- update_lsf_docs.py
- scrape_missing_lsf_docs.py
- update_lsf_docs_resume.py
- analyze_missing_commands.py
- batch_scrape_fast.py (可考虑整合)

移除临时:
- temp_batch.sh
- batch_scrape_10.sh
- sleep_script.py (功能可整合到抓取函数中)
```

### 共享文档管理
**策略**: 三类文档处理方式
1. **完全共享**: AGENTS.md, pyproject.toml等（各分支完全相同）
2. **分支定制**: README.md, HISTORY.md（相同模板，不同内容）
3. **条件共享**: 某些文档仅部分分支需要（如抓取指南）

## 执行检查清单

### 阶段检查点
- [ ] 创建备份标签 `pre-reorganization`
- [ ] 验证各分支核心功能正常
- [ ] 执行文件分类清理
- [ ] 更新各分支README和文档
- [ ] 运行验证脚本确保功能完整
- [ ] 提交更改并创建完成标签

### 质量检查
- [ ] 各分支通过 `ruff check .`
- [ ] 核心脚本运行无错误
- [ ] 文档链接和引用正确
- [ ] 无死链接或损坏文件

### 完整性验证
- [ ] 英文文档数量正确（727）
- [ ] 中文文档状态清晰
- [ ] Lumapi文档完整（86）
- [ ] 脚本功能测试通过

## 风险文件识别

### 高风险（需谨慎处理）
1. `pyproject.toml` - 依赖配置，影响所有功能
2. `AGENTS.md` - AI代理指南，影响开发工作流
3. `docs/lsf-script/en/` - 核心文档资产

### 中风险（需验证）
1. 抓取脚本 - 功能正确性影响文档更新
2. 翻译工具 - 翻译工作流依赖
3. 共享文档 - 分支间一致性

### 低风险（可安全操作）
1. 临时/备份文件 - 可安全删除
2. 测试文件 - 非生产功能
3. 日志/报告文件 - 可重新生成

## 文件处理优先级

### 优先级1：必须保留
- `docs/lsf-script/en/*.md` (727文件)
- `scripts/scrape_one_command.py`
- `scripts/update_lsf_docs.py`
- `pyproject.toml`, `uv.lock`

### 优先级2：有条件保留
- `docs/lsf-script/cn/*.md` (根据翻译质量)
- `scripts/translation_helper.py`
- `scripts/quality_assessment.py`
- 各分支README.md

### 优先级3：可移除
- 所有 `.backup` 文件
- 临时脚本文件
- 已放弃的批量翻译脚本
- 翻译分区相关文件

### 优先级4：存档专用
- `docs/lumapi/*.md` (86文件)
- `docs/lumapi-principles.md`

---

**最后更新**: 2026-02-07  
**分类依据**: 探索代理分析 + 项目HISTORY.md  
**状态**: 待执行