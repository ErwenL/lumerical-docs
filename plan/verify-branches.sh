#!/bin/bash
# 分支重组验证脚本
# 验证各分支在重组后的功能完整性

set -e  # 遇到错误时退出

echo "=== 分支重组验证测试 ==="
echo "执行时间: $(date)"
echo ""

# 颜色输出定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查当前目录是否为项目根目录
if [ ! -f "pyproject.toml" ]; then
    echo -e "${RED}错误: 请在项目根目录运行此脚本${NC}"
    exit 1
fi

# 存储验证结果
PASS_COUNT=0
FAIL_COUNT=0
SKIP_COUNT=0

# 验证函数
check_pass() {
    echo -e "${GREEN}✅ $1${NC}"
    ((PASS_COUNT++))
}

check_fail() {
    echo -e "${RED}❌ $1${NC}"
    ((FAIL_COUNT++))
}

check_skip() {
    echo -e "${YELLOW}⚠️  $1${NC}"
    ((SKIP_COUNT++))
}

# 1. 测试main分支
echo "1. 测试main分支..."
git checkout main > /dev/null 2>&1
CURRENT_BRANCH=$(git branch --show-current)
echo "   当前分支: $CURRENT_BRANCH"

# 检查文档目录
if [ -d "docs/lsf-script/en" ]; then
    EN_DOC_COUNT=$(find docs/lsf-script/en -name "*.md" 2>/dev/null | wc -l)
    echo "   英文文档数量: $EN_DOC_COUNT"
    if [ "$EN_DOC_COUNT" -ge 700 ]; then
        check_pass "英文文档完整性"
    else
        check_fail "英文文档数量不足: $EN_DOC_COUNT"
    fi
else
    check_fail "英文文档目录不存在"
fi

# 检查抓取脚本
if [ -f "scripts/scrape_one_command.py" ]; then
    python scripts/scrape_one_command.py --list > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        check_pass "抓取功能正常"
    else
        check_fail "抓取功能异常"
    fi
else
    check_fail "抓取脚本不存在"
fi

# 检查代码质量
if command -v ruff > /dev/null 2>&1; then
    ruff check . --quiet > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        check_pass "代码检查通过"
    else
        check_skip "代码检查未通过（非阻塞）"
    fi
else
    check_skip "Ruff未安装，跳过代码检查"
fi

# 检查不应存在的文件
if [ -d "docs/lsf-script/cn" ]; then
    check_fail "存在中文文档目录（应移除）"
fi

if [ -d "docs/lumapi" ]; then
    check_fail "存在Lumapi文档目录（应移除）"
fi

echo ""

# 2. 测试translation分支
echo "2. 测试translation分支..."
if git show-ref --verify --quiet refs/heads/translation; then
    git checkout translation > /dev/null 2>&1
    CURRENT_BRANCH=$(git branch --show-current)
    echo "   当前分支: $CURRENT_BRANCH"
    
    # 检查中英文文档
    if [ -d "docs/lsf-script/en" ]; then
        EN_DOC_COUNT=$(find docs/lsf-script/en -name "*.md" 2>/dev/null | wc -l)
        echo "   英文文档数量: $EN_DOC_COUNT"
    fi
    
    if [ -d "docs/lsf-script/cn" ]; then
        CN_DOC_COUNT=$(find docs/lsf-script/cn -name "*.md" 2>/dev/null | wc -l)
        echo "   中文文档数量: $CN_DOC_COUNT"
        check_pass "中文文档目录存在"
    else
        check_fail "中文文档目录不存在"
    fi
    
    # 检查翻译工具
    if [ -f "scripts/translation_helper.py" ]; then
        python scripts/translation_helper.py --stats > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            check_pass "翻译助手正常"
        else
            check_fail "翻译助手异常"
        fi
    else
        check_fail "翻译助手脚本不存在"
    fi
    
    # 检查质量工具
    if [ -f "scripts/quality_assessment.py" ]; then
        check_pass "质量评估工具存在"
    else
        check_fail "质量评估工具不存在"
    fi
    
    # 检查不应存在的批量翻译脚本
    if [ -f "scripts/auto_translate.py" ]; then
        check_fail "存在已放弃的批量翻译脚本"
    fi
    
    if [ -f "scripts/batch_translate.py" ]; then
        check_fail "存在已放弃的批量翻译脚本"
    fi
else
    echo "   translation分支不存在，跳过测试"
    check_skip "translation分支未创建"
fi

echo ""

# 3. 测试lumapi分支
echo "3. 测试lumapi分支..."
if git show-ref --verify --quiet refs/heads/lumapi; then
    git checkout lumapi > /dev/null 2>&1
    CURRENT_BRANCH=$(git branch --show-current)
    echo "   当前分支: $CURRENT_BRANCH"
    
    # 检查Lumapi文档
    if [ -d "docs/lumapi" ]; then
        LUMAPI_DOC_COUNT=$(find docs/lumapi -name "*.md" 2>/dev/null | wc -l)
        echo "   Lumapi文档数量: $LUMAPI_DOC_COUNT"
        if [ "$LUMAPI_DOC_COUNT" -ge 80 ]; then
            check_pass "Lumapi文档完整性"
        else
            check_fail "Lumapi文档数量不足: $LUMAPI_DOC_COUNT"
        fi
    else
        check_fail "Lumapi文档目录不存在"
    fi
    
    # 检查应为空的脚本目录
    SCRIPT_COUNT=$(ls scripts/*.py 2>/dev/null | wc -l)
    if [ "$SCRIPT_COUNT" -eq 0 ]; then
        check_pass "脚本目录已清理（存档分支）"
    elif [ "$SCRIPT_COUNT" -le 2 ]; then
        check_skip "脚本目录有少量文件（可接受）"
    else
        check_fail "脚本目录未充分清理: $SCRIPT_COUNT个文件"
    fi
    
    # 检查不应存在的目录
    if [ -d "docs/lsf-script" ]; then
        check_fail "存在LSF文档目录（应移除）"
    fi
else
    echo "   lumapi分支不存在，跳过测试"
    check_skip "lumapi分支未创建"
fi

echo ""

# 4. 共享文档检查
echo "4. 测试共享文档..."
git checkout main > /dev/null 2>&1

SHARED_FILES="AGENTS.md pyproject.toml .gitignore"
for file in $SHARED_FILES; do
    if [ -f "$file" ]; then
        check_pass "$file 存在"
    else
        check_fail "$file 缺失"
    fi
done

# 检查各分支README
echo ""
echo "5. 检查各分支README..."
for branch in main translation lumapi; do
    if git show-ref --verify --quiet refs/heads/$branch; then
        git checkout $branch > /dev/null 2>&1
        if [ -f "README.md" ]; then
            if grep -q "分支" README.md || grep -q "branch" README.md; then
                check_pass "$branch分支README包含分支说明"
            else
                check_skip "$branch分支README缺少分支说明"
            fi
        else
            check_fail "$branch分支缺少README.md"
        fi
    fi
done

# 返回main分支
git checkout main > /dev/null 2>&1

echo ""
echo "=== 验证结果汇总 ==="
echo "通过: $PASS_COUNT"
echo "失败: $FAIL_COUNT"
echo "跳过: $SKIP_COUNT"
echo ""

if [ $FAIL_COUNT -eq 0 ]; then
    echo -e "${GREEN}✅ 所有关键检查通过，分支重组成功${NC}"
    exit 0
else
    echo -e "${RED}❌ 发现 $FAIL_COUNT 个问题需要修复${NC}"
    echo ""
    echo "建议操作:"
    echo "1. 查看上述失败项"
    echo "2. 根据plan/project-reorganization-detailed.md修复"
    echo "3. 重新运行验证脚本"
    exit 1
fi