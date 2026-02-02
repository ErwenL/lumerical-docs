#!/usr/bin/env python3
"""
等待指定时间的脚本，用于控制抓取频率。
用法:
  python sleep_script.py           # 默认等待60秒
  python sleep_script.py 120       # 等待120秒
  python sleep_script.py --minutes 2  # 等待2分钟
"""

import argparse
import time


def main():
    parser = argparse.ArgumentParser(description="等待指定时间")
    parser.add_argument(
        "seconds", nargs="?", type=float, default=60.0, help="等待的秒数（默认: 60）"
    )
    parser.add_argument("--minutes", type=float, help="等待的分钟数")

    args = parser.parse_args()

    # 计算等待时间
    if args.minutes is not None:
        wait_time = args.minutes * 60
        unit = "分钟"
        value = args.minutes
    else:
        wait_time = args.seconds
        unit = "秒"
        value = args.seconds

    print(f"等待 {value} {unit} ({wait_time:.1f} 秒)...")

    # 显示倒计时
    if wait_time <= 10:
        # 短时间等待，直接sleep
        time.sleep(wait_time)
    else:
        # 长时间等待，显示进度
        interval = 5 if wait_time <= 60 else 30
        remaining = wait_time

        while remaining > 0:
            step = min(interval, remaining)
            time.sleep(step)
            remaining -= step
            if remaining > 0:
                print(f"  剩余 {remaining:.0f} 秒...")

    print("等待完成，可以继续下一个命令抓取。")


if __name__ == "__main__":
    main()
