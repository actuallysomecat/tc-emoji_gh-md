#!/usr/bin/env python3
"""
awkward and unnecessary thing to build a markdown document
from TootCat emoji via API request for funsies.
"""

import requests

url = "https://toot.cat/api/v1/custom_emojis"

req = requests.get(url)
res = req.json()

sorted_emoji = sorted(res, key=lambda emoji: emoji.get("category", "").lower())

title = "# Toot.Cat Emoji Cheat Sheet\n\n"
info = ("This is the output of `tc-emoji_gh-md.py` which makes an API request (via "
        "[requests](https://pypi.org/project/requests/), so you'll need that) to get the "
        "emoji at [TootCat](https://toot.cat), group them by category, and build the very "
        "`README` you are currently reading.\n\n")
table = ""
table_header = f"||Emoji|Name|Category||\n|{'|'.join([':---:']*5)}|\n"
category_list = "# Categories\n\n"

prev_category = None
for emoji in sorted_emoji:
    category = emoji.get("category", "N/A")
    if category != prev_category:
        category_list += f"* [{category}](#{category})\n"
        table += f"\n## {category}\n\n{table_header}"
    # grr html in my markdown 😾
    row = (f"| [⬆](#tootcat-emoji-cheat-sheet) "
       f"| <img src='{emoji['static_url']}' align='center' width='64'> "
       f"|`:{emoji['shortcode']}:`| {category} | "
       f"[⬆](#tootcat-emoji-cheat-sheet) |\n")
    table += row
    prev_category = category

with open("README.md", "w") as readme:
    readme.write(f"{title}{info}{category_list}{table}")

print("Wrote ./README.md! 🐱")
