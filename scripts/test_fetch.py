#!/usr/bin/env python3
import sys

sys.path.insert(0, ".")
from update_lsf_docs_resume import fetch_page

url = "https://optics.ansys.com/hc/en-us/articles/360034924793-addport-FDTD-"
print(f"Fetching {url}...")
html = fetch_page(url)
if html:
    print(f"Success! HTML length: {len(html)}")
    # Save snippet
    with open("test_output.html", "w", encoding="utf-8") as f:
        f.write(html[:5000])
    print("Saved snippet to test_output.html")
else:
    print("Failed to fetch")
