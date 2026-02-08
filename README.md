# Lumerical LSF Script Documentation Scraper

## 项目概述
专注于从Ansys Optics知识库抓取Lumerical Scripting Language (LSF)命令文档，生成本地可搜索的Markdown仓库。

## 当前状态
- **总命令数**: 727
- **已抓取**: 727个命令（100%完成）
- **文档位置**: `docs/lsf-script/en/`
- **最后更新**: 2026-02-07

## 快速开始
```bash
# 查看可用命令
python scripts/scrape_one_command.py --list

# 抓取单个命令
python scripts/scrape_one_command.py "addmaterial"

# 批量更新
python scripts/update_lsf_docs.py
```

## 安装依赖
```bash
# 使用uv（推荐）
uv sync

# 或使用pip
pip install -r requirements.txt
```

## 项目结构
```
lumerical-docs/
├── docs/lsf-script/en/     # 英文文档（727个命令）
├── scripts/                # 抓取脚本
│   ├── scrape_one_command.py      # 单命令抓取
│   ├── update_lsf_docs.py         # 批量更新
│   ├── scrape_missing_lsf_docs.py # 缺失命令抓取
│   ├── update_lsf_docs_resume.py  # 断点续传
│   ├── analyze_missing_commands.py # 分析工具
│   └── batch_scrape_fast.py       # 快速批量抓取
├── docs/                   # 项目文档
│   ├── script-commands-alphabetical.md
│   ├── script-commands-by-category.md
│   ├── missing-lsf-script-docs.md
│   └── 其他抓取相关文档
└── 配置文件
    ├── pyproject.toml
    ├── AGENTS.md
    └── .gitignore
```

## 分支结构
- `main`: LSF英文文档抓取（本分支）
- `translation`: 中文翻译工作分支
- `lumapi`: Lumapi文档存档分支

## 相关文档
- [LSF Documentation Scraping Workflow](LSF-DOCUMENTATION-SCRAPING-WORKFLOW.md) - 完整技术文档
- [Quick Start Scraping Guide](QUICK-START-SCRAPING.md) - 最小化设置指南
- [Project Completion Summary](SCRAPING-PROJECT-COMPLETION-SUMMARY.md) - 当前状态和成果
- [Agent Guidelines](AGENTS.md) - AI代理开发指南

## 开发指南
- 代码规范: 遵循AGENTS.md中的指南
- 代码检查: 使用 `ruff check .` 和 `ruff format .`
- 测试: 使用 `pytest`（测试文件待添加）

## 贡献
欢迎提交Issue和Pull Request改进抓取功能或修复文档问题。

## 许可证
本项目文档基于Ansys Optics知识库内容整理，遵循原网站的使用条款。