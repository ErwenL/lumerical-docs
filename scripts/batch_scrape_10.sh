#!/bin/bash
cd "$(dirname "$0")"
for i in {1..5}; do
    echo "抓取第 $i 条命令..."
    uv run python scrape_one_command.py --next
    echo "等待60秒..."
    uv run python sleep_script.py
done