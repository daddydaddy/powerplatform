from dotenv import load_dotenv
from collections import defaultdict
from pathlib import Path
import os
import json
import requests

# =====================================
# .env 読込
# =====================================

load_dotenv()

token = os.getenv("QIITA_TOKEN")

if not token:
    raise ValueError("QIITA_TOKEN が見つかりません")

# =====================================
# Qiita API 呼び出し
# =====================================

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    "https://qiita.com/api/v2/authenticated_user/items",
    headers=headers
)

response.raise_for_status()

articles = response.json()

# =====================================
# JSON をファイルに保存 (デバッグ用)
# =====================================

# ROOT = Path(__file__).resolve().parent.parent
# JSON_OUTPUT = ROOT / "scripts" / "qiita_articles.json"

# with open(JSON_OUTPUT, "w", encoding="utf-8") as f:
#     json.dump(articles, f, ensure_ascii=False, indent=2)

# print(f"JSON を {JSON_OUTPUT} に保存しました")

# =====================================
# タグ別に分類
# =====================================

groups = defaultdict(list)

for article in articles:

    title = article["title"]
    url = article["url"]
    stocks_count = article["stocks_count"]
    page_views_count = article["page_views_count"]
    likes_count = article["likes_count"] 
    tags = article["tags"]

    for tag in tags:

        tag_name = tag["name"]

        groups[tag_name].append({
            "title": title,
            "url": url,
            "stocks_count": stocks_count,
            "page_views_count": page_views_count, 
            "likes_count": likes_count
        })

# =====================================
# Markdown生成
# =====================================

markdown = "## Qiita記事一覧\n\n"

for tag_name in sorted(groups.keys()):

    markdown += f"## {tag_name}\n\n"

    for item in groups[tag_name]:
        markdown += f"- [{item['title']}]({item['url']}) - pageviews {item['page_views_count']}, likes {item['likes_count']},  stocks {item['stocks_count']}\n"

    markdown += "\n"

print(markdown)

# =====================================
# README読込
# =====================================

ROOT = Path(__file__).resolve().parent.parent
README_FILE = ROOT / "README.md"

with open(README_FILE, encoding="utf-8") as f:
    readme = f.read()

start_marker = "<!-- QIITA_START -->"
end_marker = "<!-- QIITA_END -->"

if start_marker not in readme:
    raise ValueError("QIITA_START が見つかりません")

if end_marker not in readme:
    raise ValueError("QIITA_END が見つかりません")

before = readme.split(start_marker)[0]
after = readme.split(end_marker)[1]

new_readme = (
    before
    + start_marker
    + "\n\n"
    + markdown
    + "\n"
    + end_marker
    + after
)

with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(new_readme)

print("README.md を更新しました")