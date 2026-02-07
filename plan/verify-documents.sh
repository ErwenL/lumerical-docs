#!/bin/bash
# 文档完整性验证脚本
# 验证各分支的文档完整性和一致性

set -e  # 遇到错误时退出

echo "=== 文档完整性验证 ==="
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

# 保存当前分支
ORIGINAL_BRANCH=$(git branch --show-current)

# 获取所有分支
ALL_BRANCHES=$(git branch --format='%(refname:short)' | sort)

echo "验证分支: $ALL_BRANCHES"
echo ""

# 文档完整性检查结果
TOTAL_CHECKS=0
PASSED_CHECKS=0
FAILED_CHECKS=0

# 检查函数
check_docs() {
    local branch=$1
    local description=$2
    local check_cmd=$3
    
    ((TOTAL_CHECKS++))
    
    if eval "$check_cmd"; then
        echo -e "  ${GREEN}✅ $description${NC}"
        ((PASSED_CHECKS++))
        return 0
    else
        echo -e "  ${RED}❌ $description${NC}"
        ((FAILED_CHECKS++))
        return 1
    fi
}

# 检查每个分支
for BRANCH in $ALL_BRANCHES; do
    echo "--- 检查分支: $BRANCH ---"
    
    # 切换到分支
    git checkout $BRANCH > /dev/null 2>&1
    
    # 基本文档检查
    check_docs "$BRANCH" "README.md存在" "[ -f README.md ]"
    check_docs "$BRANCH" "HISTORY.md存在" "[ -f HISTORY.md ]"
    check_docs "$BRANCH" "AGENTS.md存在" "[ -f AGENTS.md ]"
    
    # 分支特定文档检查
    case $BRANCH in
        main)
            check_docs "$BRANCH" "英文文档目录存在" "[ -d docs/lsf-script/en ]"
            if [ -d docs/lsf-script/en ]; then
                EN_COUNT=$(find docs/lsf-script/en -name "*.md" 2>/dev/null | wc -l)
                echo "    英文文档数量: $EN_COUNT"
                if [ "$EN_COUNT" -ge 700 ]; then
                    echo -e "    ${GREEN}✅ 英文文档数量充足${NC}"
                else
                    echo -e "    ${YELLOW}⚠  英文文档数量可能不足${NC}"
                fi
            fi
            
            # 检查不应存在的文档
            if [ -d docs/lsf-script/cn ]; then
                echo -e "    ${RED}❌ 存在中文文档目录（应移除）${NC}"
                ((FAILED_CHECKS++))
            fi
            
            if [ -d docs/lumapi ]; then
                echo -e "    ${RED}❌ 存在Lumapi文档目录（应移除）${NC}"
                ((FAILED_CHECKS++))
            fi
            ;;
        
        translation)
            check_docs "$BRANCH" "英文文档目录存在" "[ -d docs/lsf-script/en ]"
            check_docs "$BRANCH" "中文文档目录存在" "[ -d docs/lsf-script/cn ]"
            
            if [ -d docs/lsf-script/en ] && [ -d docs/lsf-script/cn ]; then
                EN_COUNT=$(find docs/lsf-script/en -name "*.md" 2>/dev/null | wc -l)
                CN_COUNT=$(find docs/lsf-script/cn -name "*.md" 2>/dev/null | wc -l)
                echo "    英文文档数量: $EN_COUNT"
                echo "    中文文档数量: $CN_COUNT"
                
                # 计算翻译进度
                if [ "$EN_COUNT" -gt 0 ]; then
                    PROGRESS=$((CN_COUNT * 100 / EN_COUNT))
                    echo "    翻译进度: $PROGRESS%"
                fi
            fi
            
            # 检查翻译工具文档
            check_docs "$BRANCH" "翻译进度文件存在" "[ -f docs/translation-progress.json ]"
            
            # 检查不应存在的批量翻译文件
            if [ -d docs/translation-sections ]; then
                echo -e "    ${YELLOW}⚠  存在翻译分区目录（已放弃功能）${NC}"
            fi
            ;;
        
        lumapi)
            check_docs "$BRANCH" "Lumapi文档目录存在" "[ -d docs/lumapi ]"
            
            if [ -d docs/lumapi ]; then
                LUMAPI_COUNT=$(find docs/lumapi -name "*.md" 2>/dev/null | wc -l)
                echo "    Lumapi文档数量: $LUMAPI_COUNT"
                if [ "$LUMAPI_COUNT" -ge 80 ]; then
                    echo -e "    ${GREEN}✅ Lumapi文档数量充足${NC}"
                else
                    echo -e "    ${YELLOW}⚠  Lumapi文档数量可能不足${NC}"
                fi
            fi
            
            # 检查原理文档
            check_docs "$BRANCH" "Lumapi原理文档存在" "[ -f docs/lumapi-principles.md ]"
            
            # 检查不应存在的文档
            if [ -d docs/lsf-script ]; then
                echo -e "    ${RED}❌ 存在LSF文档目录（应移除）${NC}"
                ((FAILED_CHECKS++))
            fi
            ;;
    esac
    
    # 检查共享文档
    echo "    共享文档检查:"
    SHARED_DOCS="pyproject.toml .gitignore"
    for doc in $SHARED_DOCS; do
        if [ -f "$doc" ]; then
            echo -e "      ${GREEN}✓ $doc${NC}"
        else
            echo -e "      ${RED}✗ $doc 缺失${NC}"
            ((FAILED_CHECKS++))
        fi
        ((TOTAL_CHECKS++))
    done
    
    echo ""
done

# 返回原始分支
git checkout $ORIGINAL_BRANCH > /dev/null 2>&1

echo "=== 验证结果汇总 ==="
echo "总检查项: $TOTAL_CHECKS"
echo "通过项: $PASSED_CHECKS"
echo "失败项: $FAILED_CHECKS"
echo ""

if [ $FAILED_CHECKS -eq 0 ]; then
    echo -e "${GREEN}✅ 所有文档检查通过${NC}"
else
    echo -e "${RED}❌ 发现 $FAILED_CHECKS 个文档问题${NC}"
    echo ""
    echo "常见问题修复:"
    echo "1. 缺失README.md - 创建分支特定README"
    echo "2. 文档目录错误 - 根据分支规范清理目录"
    echo "3. 共享文档缺失 - 运行同步脚本: ./plan/sync-shared-docs.sh --all"
fi

echo ""
echo "=== 文档统计 ==="

# 生成详细统计
for BRANCH in $ALL_BRANCHES; do
    git checkout $BRANCH > /dev/null 2>&1
    
    echo "分支: $BRANCH"
    
    # 统计各类文档
    if [ -d docs ]; then
        echo "  文档目录结构:"
        find docs -type f -name "*.md" | sed 's|^|    |' | head -10
        
        MD_COUNT=$(find docs -type f -name "*.md" 2>/dev/null | wc -l)
        JSON_COUNT=$(find docs -type f -name "*.json" 2>/dev/null | wc -l)
        echo "  Markdown文件: $MD_COUNT"
        echo "  JSON文件: $JSON_COUNT"
    else
        echo "  文档目录不存在"
    fi
    
    # 检查文档质量（简单检查）
    echo "  文档质量检查:"
    
    # 检查README是否包含分支信息
    if [ -f README.md ]; then
        if grep -q -i "branch\|分支" README.md; then
            echo -e "    ${GREEN}✓ README包含分支说明${NC}"
        else
            echo -e "    ${YELLOW}⚠  README缺少分支说明${NC}"
        fi
    fi
    
    # 检查HISTORY是否更新
    if [ -f HISTORY.md ]; then
        if grep -q -i "2026\|重组" HISTORY.md; then
            echo -e "    ${GREEN}✓ HISTORY包含最近更新${NC}"
        else
            echo -e "    ${YELLOW}⚠  HISTORY可能未更新${NC}"
        fi
    fi
    
    echo ""
done

# 返回原始分支
git checkout $ORIGINAL_BRANCH > /dev/null 2>&1

echo "=== 建议与后续操作 ==="
echo ""
echo "1. 文档同步:"
echo "   运行 ./plan/sync-shared-docs.sh --all"
echo "   同步共享文档到所有分支"
echo ""
echo "2. 分支特定文档:"
echo "   确保各分支README.md和HISTORY.md适当更新"
echo "   main分支: 聚焦LSF抓取"
echo "   translation分支: 说明翻译工作流程"
echo "   lumapi分支: 说明存档状态"
echo ""
echo "3. 文档清理:"
echo "   移除不应存在的文档目录"
echo "   清理已放弃功能的文件"
echo ""
echo "4. 定期检查:"
echo "   每月运行此验证脚本"
echo "   保持文档与分支状态同步"

echo ""
echo "=== 验证完成 ==="