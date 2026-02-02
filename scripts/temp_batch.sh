#!/bin/bash
cd "$(dirname "$0")"
for i in {1..5}; do
    echo "批量抓取第 $i 次..."
    timeout 130 uv run python scrape_missing_lsf_docs.py >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "第 $i 次抓取成功"
    else
        echo "第 $i 次抓取可能超时，但可能已完成"
    fi
done
echo "批量抓取完成"