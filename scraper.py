import requests
from bs4 import BeautifulSoup
import csv

# Yahoo!ニュース トップページ
url = "https://news.yahoo.co.jp/"

# HTML取得
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# 見出しリストを取得（主要ニュース）
headlines = soup.select("a[href^='https://news.yahoo.co.jp/articles']")

# 重複排除用セット
seen = set()

# 出力ファイル設定
csv_filename = "news.csv"

# コンソール出力
print("【Yahoo!ニュース 見出し一覧】")

news_list = []
for a in headlines:
    title = a.get_text(strip=True)
    link = a["href"]

    if link not in seen and title:
        news_list.append((title, link))
        print(f"{len(news_list)}. {title}")
        print(f"   URL: {link}")
        seen.add(link)

    if len(news_list) >= 10:
        break

# CSV保存
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "URL"])  # ヘッダー
    writer.writerows(news_list)

print(f"\n✅ Saved to '{csv_filename}'")
