import requests
from bs4 import BeautifulSoup

# Yahoo!ニュース トップページ
url = "https://news.yahoo.co.jp/"

# HTML取得
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# 見出しリストを取得（主要ニュース）
headlines = soup.select("a[href^='https://news.yahoo.co.jp/articles']")

# 表示（重複しないようsetで制限）
seen = set()
count = 0

print("【Yahoo!ニュース 見出し一覧】")
for a in headlines:
    title = a.get_text(strip=True)
    link = a["href"]

    if link not in seen and title:
        print(f"{count+1}. {title}")
        print(f"   URL: {link}")
        seen.add(link)
        count += 1

    if count >= 10:
        break
