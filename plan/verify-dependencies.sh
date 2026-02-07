#!/bin/bash
# 依赖一致性验证脚本
# 验证各分支的依赖配置是否一致

set -e  # 遇到错误时退出

echo "=== 依赖一致性验证 ==="
echo "执行时间: $(date)"
echo ""

# 颜色输出定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查当前目录
if [ ! -f "pyproject.toml" ]; then
    echo -e "${RED}错误: 请在项目根目录运行此脚本${NC}"
    exit 1
fi

# 关键依赖列表
CORE_DEPENDENCIES="beautifulsoup4 cloudscraper html2text requests selenium webdriver-manager"
OPTIONAL_DEPENDENCIES="mdformat mdformat-tables tqdm"
DEV_DEPENDENCIES="ruff pytest"

# 保存当前分支
ORIGINAL_BRANCH=$(git branch --show-current)

# 获取所有分支
ALL_BRANCHES=$(git branch --format='%(refname:short)' | sort)

echo "项目分支:"
for branch in $ALL_BRANCHES; do
    echo "  - $branch"
done
echo ""

# 检查每个分支
BRANCH_COUNT=0
CONSISTENT_BRANCHES=0
ISSUE_COUNT=0

for BRANCH in $ALL_BRANCHES; do
    echo "检查分支: $BRANCH"
    
    # 切换到分支
    git checkout $BRANCH > /dev/null 2>&1
    
    # 检查pyproject.toml是否存在
    if [ ! -f "pyproject.toml" ]; then
        echo -e "  ${RED}❌ pyproject.toml 不存在${NC}"
        ((ISSUE_COUNT++))
        continue
    fi
    
    echo -e "  ${GREEN}✅ pyproject.toml 存在${NC}"
    
    # 检查关键依赖
    MISSING_CORE=0
    for dep in $CORE_DEPENDENCIES; do
        if grep -q "$dep" pyproject.toml; then
            echo -e "    ${GREEN}✓ 包含 $dep${NC}"
        else
            echo -e "    ${YELLOW}⚠  缺少 $dep${NC}"
            ((MISSING_CORE++))
        fi
    done
    
    # 检查Python版本
    PYTHON_VERSION=$(grep "requires-python" pyproject.toml | sed 's/.*= *"\(.*\)"/\1/')
    if [ -n "$PYTHON_VERSION" ]; then
        echo -e "    ${GREEN}✓ Python版本: $PYTHON_VERSION${NC}"
    else
        echo -e "    ${YELLOW}⚠  Python版本未指定${NC}"
    fi
    
    # 检查项目名称
    PROJECT_NAME=$(grep "^name =" pyproject.toml | sed 's/.*= *"\(.*\)"/\1/')
    if [ -n "$PROJECT_NAME" ]; then
        echo -e "    ${GREEN}✓ 项目名称: $PROJECT_NAME${NC}"
    else
        echo -e "    ${YELLOW}⚠  项目名称未指定${NC}"
    fi
    
    # 检查uv.lock是否存在
    if [ -f "uv.lock" ]; then
        echo -e "    ${GREEN}✓ uv.lock 存在${NC}"
    else
        echo -e "    ${YELLOW}⚠  uv.lock 不存在${NC}"
    fi
    
    # 检查requirements.txt（可选）
    if [ -f "requirements.txt" ]; then
        echo -e "    ${GREEN}✓ requirements.txt 存在${NC}"
    else
        echo -e "    ${YELLOW}⚠  requirements.txt 不存在（可选）${NC}"
    fi
    
    # 分支特定检查
    case $BRANCH in
        main)
            # main分支需要完整抓取依赖
            if [ $MISSING_CORE -eq 0 ]; then
                echo -e "    ${GREEN}✅ 抓取依赖完整${NC}"
                ((CONSISTENT_BRANCHES++))
            else
                echo -e "    ${YELLOW}⚠  抓取依赖不完整${NC}"
            fi
            ;;
        translation)
            # translation分支需要抓取和翻译依赖
            if [ $MISSING_CORE -eq 0 ]; then
                echo -e "    ${GREEN}✅ 抓取依赖完整（翻译需要）${NC}"
                ((CONSISTENT_BRANCHES++))
            else
                echo -e "    ${YELLOW}⚠  抓取依赖不完整${NC}"
            fi
            ;;
        lumapi)
            # lumapi分支依赖要求最低
            echo -e "    ${GREEN}✅ 存档分支依赖检查通过${NC}"
            ((CONSISTENT_BRANCHES++))
            ;;
        *)
            # 其他分支
            echo -e "    ${GREEN}✅ 分支依赖检查通过${NC}"
            ((CONSISTENT_BRANCHES++))
            ;;
    esac
    
    ((BRANCH_COUNT++))
    echo ""
done

# 返回原始分支
git checkout $ORIGINAL_BRANCH > /dev/null 2>&1

echo "=== 验证结果 ==="
echo "检查分支数: $BRANCH_COUNT"
echo "一致分支数: $CONSISTENT_BRANCHES"
echo "发现问题数: $ISSUE_COUNT"
echo ""

# 依赖对比
echo "=== 依赖对比 ==="
echo "比较各分支的pyproject.toml内容差异..."

# 收集所有分支的pyproject.toml哈希值
declare -A BRANCH_HASHES
for BRANCH in $ALL_BRANCHES; do
    if git show $BRANCH:pyproject.toml > /dev/null 2>&1; then
        HASH=$(git show $BRANCH:pyproject.toml | shasum -a 256 | cut -d' ' -f1)
        BRANCH_HASHES[$BRANCH]=$HASH
    fi
done

# 找出不同的哈希值
declare -A HASH_GROUPS
for BRANCH in "${!BRANCH_HASHES[@]}"; do
    HASH=${BRANCH_HASHES[$BRANCH]}
    HASH_GROUPS[$HASH]="${HASH_GROUPS[$HASH]} $BRANCH"
done

echo "依赖配置分组:"
GROUP_COUNT=0
for HASH in "${!HASH_GROUPS[@]}"; do
    ((GROUP_COUNT++))
    BRANCHES=${HASH_GROUPS[$HASH]}
    BRANCH_LIST=$(echo $BRANCHES | sed 's/^ //')
    echo "  组 $GROUP_COUNT: $BRANCH_LIST"
done

if [ $GROUP_COUNT -eq 1 ]; then
    echo -e "${GREEN}✅ 所有分支依赖配置完全一致${NC}"
else
    echo -e "${YELLOW}⚠  发现 $GROUP_COUNT 种不同的依赖配置${NC}"
    echo ""
    echo "建议:"
    echo "1. 确保核心分支(main, translation)依赖一致"
    echo "2. lumapi分支可以使用精简依赖"
    echo "3. 运行 ./plan/sync-shared-docs.sh --all 同步配置"
fi

echo ""
echo "=== 详细建议 ==="

# 检查main分支的依赖完整性
echo "1. main分支依赖检查:"
git checkout main > /dev/null 2>&1
if [ -f "pyproject.toml" ]; then
    echo "   项目名称: $(grep '^name =' pyproject.toml | sed 's/.*= *"\(.*\)"/\1/')"
    echo "   Python版本: $(grep 'requires-python' pyproject.toml | sed 's/.*= *"\(.*\)"/\1/')"
    
    # 检查关键依赖
    echo "   关键依赖状态:"
    for dep in $CORE_DEPENDENCIES; do
        if grep -q "$dep" pyproject.toml; then
            echo -e "     ${GREEN}✓ $dep${NC}"
        else
            echo -e "     ${RED}✗ $dep (缺失)${NC}"
        fi
    done
fi
git checkout $ORIGINAL_BRANCH > /dev/null 2>&1

echo ""
echo "2. 依赖管理建议:"
cat << EOF
   - 所有分支共享 pyproject.toml 和 uv.lock
   - 使用 uv sync 安装依赖
   - 添加新依赖: uv add <package>
   - 添加开发依赖: uv add --dev <package>
   - 更新依赖: uv sync --upgrade
EOF

echo ""
echo "3. 问题解决:"
if [ $ISSUE_COUNT -gt 0 ]; then
    echo -e "   ${RED}发现 $ISSUE_COUNT 个问题需要处理${NC}"
    echo "   建议步骤:"
    echo "   1. 修复缺失的pyproject.toml文件"
    echo "   2. 确保关键依赖存在"
    echo "   3. 重新运行此验证脚本"
else
    echo -e "   ${GREEN}依赖配置基本正常${NC}"
fi

echo ""
echo "4. 后续操作:"
echo "   运行 ./plan/verify-branches.sh 验证各分支功能"
echo "   运行 ./plan/sync-shared-docs.sh --all 同步共享文档"