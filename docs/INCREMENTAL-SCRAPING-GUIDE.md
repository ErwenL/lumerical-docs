# 增量抓取操作指南

## 当前状态 (2026-02-02)

- **总命令数**: 727 个
- **已抓取文档**: 639 个 (`docs/lsf-script/`)
- **缺失命令**: 189 个 (`docs/missing-lsf-script-docs.md`)
- **完成率**: 约 87.9%
- **最近抓取**: `addport (FDTD)` 成功抓取并已从缺失列表中移除

## 可用脚本

### 1. 单次抓取脚本 (`scripts/scrape_one_command.py`)

**功能**: 每次只抓取一个命令文档，支持多种操作模式。

**用法**:
```bash
# 显示缺失命令列表（前20个）
python scripts/scrape_one_command.py --list

# 显示统计信息
python scripts/scrape_one_command.py --stats

# 抓取下一个缺失命令（按列表顺序）
python scripts/scrape_one_command.py --next

# 抓取指定命令（需完整命令名）
python scripts/scrape_one_command.py "addport (INTERCONNECT)"

# 显示帮助
python scripts/scrape_one_command.py --help
```

**工作流程**:
1. 从 `missing-lsf-script-docs.md` 读取命令列表
2. 使用 cloudscraper + selenium 备选方案抓取页面
3. 提取内容并保存为 Markdown 文件到 `docs/lsf-script/`
4. 成功时：更新进度文件 `docs/scrape-progress.json`，并从缺失列表中移除
5. 失败时：记录日志，保持命令在列表中以便重试

### 2. 等待脚本 (`scripts/sleep_script.py`)

**功能**: 控制抓取频率，避免请求过载。

**用法**:
```bash
# 默认等待60秒
python scripts/sleep_script.py

# 等待指定秒数
python scripts/sleep_script.py 120

# 等待指定分钟数
python scripts/sleep_script.py --minutes 2

# 显示帮助
python scripts/sleep_script.py --help
```

## 推荐工作流程

### 选项A：手动控制（推荐）
```bash
# 步骤1：查看当前状态
python scripts/scrape_one_command.py --stats

# 步骤2：查看可用的缺失命令
python scripts/scrape_one_command.py --list

# 步骤3：抓取指定命令
python scripts/scrape_one_command.py "command_name"

# 步骤4：等待60秒（避免请求过载）
python scripts/sleep_script.py

# 重复步骤2-4
```

### 选项B：自动顺序抓取
```bash
# 抓取下一个命令，然后等待60秒
python scripts/scrape_one_command.py --next && python scripts/sleep_script.py

# 或者使用循环（谨慎使用，可能因网络问题中断）
for i in {1..10}; do
    python scripts/scrape_one_command.py --next
    python scripts/sleep_script.py
done
```

### 选项C：批量处理
```bash
# 每次会话处理5-10个命令
for i in {1..5}; do
    echo "处理第 $i 个命令..."
    python scripts/scrape_one_command.py --next
    python scripts/sleep_script.py
done
```

## 当前建议

基于当前进度（189个缺失命令），建议：

1. **先测试网络稳定性**：抓取2-3个命令验证 cloudscraper 是否正常工作
2. **按字母顺序处理**：缺失命令主要集中在 C, N, O, P, R, S, T, V, W, Z 等字母
3. **合理控制频率**：每个命令之间等待60-120秒，避免触发 Cloudflare 防护

## 缺失命令分布

根据 `missing-lsf-script-docs.md`，缺失命令按字母分组：

- **A**: 2个命令（可能已部分抓取）
- **C**: 7个命令（cross, ctranspose, currentfilename, currentscriptname, customlibrary, cwnorm, czt）
- **N**: 8个命令（newwizard, newwizardpage, nonorm, norm, normpdf, now, num2str, nummodes）
- **O**: 4个命令（optimizeposition, or, orbit, overlap）
- **P**: 许多命令（从 partitionvolume 开始）
- **R, S, T, V, W, Z**: 均有缺失命令

## 故障排除

### 常见问题

1. **网络超时/Cloudflare拦截**
   - 现象：脚本长时间挂起或返回超时错误
   - 解决：cloudscraper 会自动重试5次，然后切换到 selenium 备选方案
   - 建议：增加等待时间（使用 `sleep_script.py 120`）

2. **Unicode编码错误**
   - 现象：Windows控制台显示编码错误
   - 解决：脚本已修复大部分Unicode字符，使用ASCII替代

3. **命令已存在但仍列在缺失列表中**
   - 现象：某些命令可能已有文档文件
   - 解决：脚本会自动跳过已处理的命令（基于进度文件）

4. **进度文件损坏**
   - 现象：`scrape-progress.json` 无法读取
   - 解决：删除该文件，脚本会重新创建

### 日志文件

- **单次抓取日志**: `docs/scrape-single.log`
- **进度追踪**: `docs/scrape-progress.json`
- **原始日志**: `docs/scrape.log`（之前运行的历史记录）

## 下一步操作建议

### 立即行动
1. 测试抓取下一个命令：`python scripts/scrape_one_command.py --next`
2. 等待60秒：`python scripts/sleep_script.py`
3. 重复上述步骤处理5-10个命令

### 长期计划
- 每天处理20-30个命令（约需1-2小时）
- 优先处理常用命令（根据字母C, N, O开头的命令）
- 定期验证已抓取文档的完整性

## 注意事项

1. **网络稳定性**: Ansys网站有时响应较慢，需耐心等待
2. **请求频率**: 避免高频请求，建议每分钟不超过1个请求
3. **进度保存**: 每次成功抓取后会自动保存进度，可随时中断和恢复
4. **文件命名**: 特殊字符的命令名会进行安全文件名转换

## 紧急恢复

如果抓取过程出现问题：

1. **检查当前进度**:
   ```bash
   python scripts/scrape_one_command.py --stats
   ```

2. **查看最后抓取的命令**:
   ```bash
   tail -5 docs/scrape-single.log
   ```

3. **手动从缺失列表中移除命令**（如果需要）:
   - 编辑 `docs/missing-lsf-script-docs.md`
   - 删除对应的表格行

4. **重置进度**（慎用）:
   ```bash
   rm docs/scrape-progress.json
   ```

---

**最后更新**: 2026-02-02  
**更新者**: AI Assistant  
**状态**: 准备就绪，等待开始增量抓取