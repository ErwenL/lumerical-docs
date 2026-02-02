#!/usr/bin/env python3
"""
批量抓取指定数量的命令，保持60秒间隔。
"""

import subprocess
import sys


def run_command(cmd):
    """运行命令并返回输出"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)


def main():
    if len(sys.argv) < 2:
        print("用法: python batch_scrape_fast.py <数量>")
        print("示例: python batch_scrape_fast.py 10")
        return

    try:
        count = int(sys.argv[1])
    except ValueError:
        print("错误: 参数必须是整数")
        return

    print(f"开始批量抓取 {count} 条命令...")

    for i in range(1, count + 1):
        print(f"\n=== 抓取第 {i}/{count} 条命令 ===")

        # 抓取命令
        retcode, stdout, stderr = run_command(
            "uv run python scrape_one_command.py --next"
        )

        # 提取关键信息
        if "SUCCESS" in stdout or "成功" in stdout:
            print(f"[OK] 第 {i} 条命令抓取成功")
        elif "FAILED" in stdout or "失败" in stdout:
            print(f"[FAIL] 第 {i} 条命令抓取失败")
        else:
            # 尝试从输出中提取信息
            lines = stdout.split("\n")
            for line in lines:
                if "剩余待抓取命令数" in line or "ʣ���ץȡ������" in line:
                    print(line.strip())
                    break

        # 如果不是最后一条命令，等待60秒
        if i < count:
            print(f"等待60秒 ({i}/{count})...")
            # 使用sleep_script.py等待
            run_command("uv run python sleep_script.py")

    print(f"\n批量抓取完成，共处理 {count} 条命令")


if __name__ == "__main__":
    main()
