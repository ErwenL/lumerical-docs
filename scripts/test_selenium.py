#!/usr/bin/env python3
import sys

sys.path.insert(0, ".")
from update_lsf_docs_resume import fetch_page_selenium

url = "https://optics.ansys.com/hc/en-us/articles/360034924793-addport-FDTD-"
print("Testing selenium fetch...")
html = fetch_page_selenium(url)
if html:
    print(f"Success! HTML length: {len(html)}")
else:
    print("Failed")
