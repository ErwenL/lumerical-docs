#!/bin/bash
# 共享文档同步脚本
# 将共享文档从一个分支同步到其他分支

set -e  # 遇到错误时退出

# 颜色输出定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 共享文档列表
SHARED_FILES="AGENTS.md pyproject.toml uv.lock .gitignore requirements.txt"
CONDITIONAL_FILES="LSF-DOCUMENTATION-SCRAPING-WORKFLOW.md QUICK-START-SCRAPING.md SCRAPING-PROJECT-COMPLETION-SUMMARY.md"

# 显示帮助信息
show_help() {
    cat << EOF
共享文档同步脚本

用法: $0 [选项] [分支名]

选项:
  --all                同步到所有分支 (main, translation, lumapi)
  --from <branch>      从指定分支获取源文件 (默认: main)
  --dry-run           模拟运行，不实际修改文件
  --list              列出共享文档列表
  --help              显示此帮助信息

示例:
  $0 --all                    # 从main同步到所有分支
  $0 translation              # 从main同步到translation分支
  $0 --from translation --all # 从translation同步到所有分支
  $0 --dry-run --all          # 模拟同步操作
  $0 --list                   # 列出共享文档

共享文档说明:
  完全共享: ${SHARED_FILES}
  条件共享: ${CONDITIONAL_FILES}
  分支特定: README.md, HISTORY.md, docs/目录内容
EOF
}

# 检查参数
if [ $# -eq 0 ]; then
    show_help
    exit 0
fi

# 初始化变量
TARGET_BRANCHES=""
SOURCE_BRANCH="main"
DRY_RUN=false
LIST_MODE=false

# 解析参数
while [ $# -gt 0 ]; do
    case $1 in
        --all)
            TARGET_BRANCHES="main translation lumapi"
            ;;
        --from)
            shift
            SOURCE_BRANCH=$1
            ;;
        --dry-run)
            DRY_RUN=true
            ;;
        --list)
            LIST_MODE=true
            ;;
        --help)
            show_help
            exit 0
            ;;
        -*)
            echo -e "${RED}错误: 未知选项 $1${NC}"
            show_help
            exit 1
            ;;
        *)
            if [ -z "$TARGET_BRANCHES" ]; then
                TARGET_BRANCHES=$1
            else
                TARGET_BRANCHES="$TARGET_BRANCHES $1"
            fi
            ;;
    esac
    shift
done

# 列表模式
if [ "$LIST_MODE" = true ]; then
    echo "=== 共享文档列表 ==="
    echo ""
    echo "完全共享文档 (所有分支相同):"
    for file in $SHARED_FILES; do
        echo "  - $file"
    done
    echo ""
    echo "条件共享文档 (部分分支需要):"
    for file in $CONDITIONAL_FILES; do
        echo "  - $file (main和translation分支需要)"
    done
    echo ""
    echo "分支特定文档 (各分支不同):"
    echo "  - README.md"
    echo "  - HISTORY.md"
    echo "  - docs/ 目录内容"
    echo ""
    exit 0
fi

# 检查当前目录
if [ ! -f "pyproject.toml" ]; then
    echo -e "${RED}错误: 请在项目根目录运行此脚本${NC}"
    exit 1
fi

# 检查源分支是否存在
if ! git show-ref --verify --quiet refs/heads/$SOURCE_BRANCH; then
    echo -e "${RED}错误: 源分支 '$SOURCE_BRANCH' 不存在${NC}"
    echo "可用分支:"
    git branch -a | grep -v "remotes/" | sed 's/^* //' | sed 's/^/  /'
    exit 1
fi

# 如果没有指定目标分支，使用当前分支
if [ -z "$TARGET_BRANCHES" ]; then
    CURRENT_BRANCH=$(git branch --show-current)
    TARGET_BRANCHES=$CURRENT_BRANCH
    echo -e "${YELLOW}警告: 未指定目标分支，将同步到当前分支 ($CURRENT_BRANCH)${NC}"
    echo ""
fi

# 显示同步信息
echo "=== 共享文档同步 ==="
echo "源分支: $SOURCE_BRANCH"
echo "目标分支: $TARGET_BRANCHES"
echo "模式: $([ "$DRY_RUN" = true ] && echo "模拟运行" || echo "实际执行")"
echo ""

# 保存当前分支
ORIGINAL_BRANCH=$(git branch --show-current)

# 切换到源分支获取文件
echo "从源分支 '$SOURCE_BRANCH' 获取文件..."
git checkout $SOURCE_BRANCH > /dev/null 2>&1

# 创建临时目录存储源文件
TEMP_DIR=$(mktemp -d)
echo "创建临时目录: $TEMP_DIR"

# 复制共享文件到临时目录
COPIED_COUNT=0
for file in $SHARED_FILES; do
    if [ -f "$file" ]; then
        cp "$file" "$TEMP_DIR/"
        ((COPIED_COUNT++))
        if [ "$DRY_RUN" = true ]; then
            echo "  [模拟] 复制: $file"
        else
            echo "  复制: $file"
        fi
    else
        echo -e "${YELLOW}  警告: $file 在源分支不存在${NC}"
    fi
done

# 复制条件共享文件（可选）
for file in $CONDITIONAL_FILES; do
    if [ -f "$file" ]; then
        cp "$file" "$TEMP_DIR/"
        ((COPIED_COUNT++))
        if [ "$DRY_RUN" = true ]; then
            echo "  [模拟] 复制: $file (条件共享)"
        else
            echo "  复制: $file (条件共享)"
        fi
    fi
done

echo "总计复制 $COPIED_COUNT 个文件"
echo ""

# 同步到每个目标分支
SYNCED_BRANCHES=0
for TARGET_BRANCH in $TARGET_BRANCHES; do
    echo "--- 同步到分支: $TARGET_BRANCH ---"
    
    # 检查目标分支是否存在
    if ! git show-ref --verify --quiet refs/heads/$TARGET_BRANCH; then
        echo -e "${YELLOW}  跳过: 分支 '$TARGET_BRANCH' 不存在${NC}"
        continue
    fi
    
    # 切换到目标分支
    if [ "$DRY_RUN" = true ]; then
        echo "  [模拟] 切换到分支: $TARGET_BRANCH"
    else
        git checkout $TARGET_BRANCH > /dev/null 2>&1
        echo "  切换到分支: $TARGET_BRANCH"
    fi
    
    # 同步每个文件
    SYNCED_FILES=0
    for file in $SHARED_FILES; do
        SRC_FILE="$TEMP_DIR/$file"
        if [ -f "$SRC_FILE" ]; then
            # 检查文件是否不同
            if [ -f "$file" ]; then
                if ! cmp -s "$SRC_FILE" "$file"; then
                    if [ "$DRY_RUN" = true ]; then
                        echo "  [模拟] 更新: $file (内容不同)"
                    else
                        cp "$SRC_FILE" "$file"
                        echo "  更新: $file (内容不同)"
                    fi
                    ((SYNCED_FILES++))
                else
                    echo "  跳过: $file (内容相同)"
                fi
            else
                if [ "$DRY_RUN" = true ]; then
                    echo "  [模拟] 添加: $file (新文件)"
                else
                    cp "$SRC_FILE" "$file"
                    echo "  添加: $file (新文件)"
                fi
                ((SYNCED_FILES++))
            fi
        fi
    done
    
    # 条件共享文件处理（根据分支类型）
    for file in $CONDITIONAL_FILES; do
        SRC_FILE="$TEMP_DIR/$file"
        if [ -f "$SRC_FILE" ]; then
            # 确定是否需要此文件
            NEED_FILE=false
            case $TARGET_BRANCH in
                main|translation)
                    NEED_FILE=true
                    ;;
                lumapi)
                    NEED_FILE=false  # lumapi分支不需要抓取文档
                    ;;
                *)
                    NEED_FILE=true  # 默认需要
                    ;;
            esac
            
            if [ "$NEED_FILE" = true ]; then
                if [ -f "$file" ]; then
                    if ! cmp -s "$SRC_FILE" "$file"; then
                        if [ "$DRY_RUN" = true ]; then
                            echo "  [模拟] 更新: $file (条件共享，内容不同)"
                        else
                            cp "$SRC_FILE" "$file"
                            echo "  更新: $file (条件共享，内容不同)"
                        fi
                        ((SYNCED_FILES++))
                    else
                        echo "  跳过: $file (条件共享，内容相同)"
                    fi
                else
                    if [ "$DRY_RUN" = true ]; then
                        echo "  [模拟] 添加: $file (条件共享，新文件)"
                    else
                        cp "$SRC_FILE" "$file"
                        echo "  添加: $file (条件共享，新文件)"
                    fi
                    ((SYNCED_FILES++))
                fi
            else
                # 如果目标分支不需要此文件，但文件存在，则删除
                if [ -f "$file" ]; then
                    if [ "$DRY_RUN" = true ]; then
                        echo "  [模拟] 删除: $file (条件共享，本分支不需要)"
                    else
                        rm "$file"
                        echo "  删除: $file (条件共享，本分支不需要)"
                    fi
                fi
            fi
        fi
    done
    
    echo "  本分支同步文件数: $SYNCED_FILES"
    
    # 提交更改（如果不是模拟运行）
    if [ "$SYNCED_FILES" -gt 0 ] && [ "$DRY_RUN" = false ]; then
        git add $SHARED_FILES $CONDITIONAL_FILES 2>/dev/null || true
        CHANGED_FILES=$(git status --porcelain | grep -E "^(M|A|D)" | wc -l)
        if [ "$CHANGED_FILES" -gt 0 ]; then
            git commit -m "chore: sync shared documents from $SOURCE_BRANCH" > /dev/null
            echo "  已提交更改"
        fi
    fi
    
    ((SYNCED_BRANCHES++))
    echo ""
done

# 清理临时目录
rm -rf "$TEMP_DIR"
echo "清理临时目录"

# 返回原始分支
if [ "$DRY_RUN" = false ]; then
    git checkout $ORIGINAL_BRANCH > /dev/null 2>&1
    echo "返回原始分支: $ORIGINAL_BRANCH"
fi

echo ""
echo "=== 同步完成 ==="
echo "源分支: $SOURCE_BRANCH"
echo "成功同步分支数: $SYNCED_BRANCHES"
echo "复制文件总数: $COPIED_COUNT"

if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}注意: 本次为模拟运行，未实际修改文件${NC}"
    echo "要实际执行，请移除 --dry-run 参数"
else
    echo -e "${GREEN}✅ 共享文档同步完成${NC}"
fi

echo ""
echo "后续建议:"
echo "1. 运行验证脚本检查各分支状态: ./plan/verify-branches.sh"
echo "2. 定期运行此脚本保持文档同步"
echo "3. 更新分支特定文档 (README.md, HISTORY.md)"