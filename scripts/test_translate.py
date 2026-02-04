#!/usr/bin/env python3
"""测试翻译功能。"""

import sys
from pathlib import Path

# 添加当前目录到路径
sys.path.insert(0, str(Path(__file__).parent))

try:
    from googletrans import Translator
    print("googletrans导入成功")
    
    # 测试翻译
    translator = Translator()
    result = translator.translate("Hello world", src='en', dest='zh-cn')
    print(f"测试翻译: 'Hello world' -> '{result.text}'")
    print("翻译功能正常")
    
except ImportError as e:
    print(f"导入googletrans失败: {e}")
    print("尝试安装: pip install googletrans==4.0.0rc1")
except Exception as e:
    print(f"翻译测试失败: {e}")