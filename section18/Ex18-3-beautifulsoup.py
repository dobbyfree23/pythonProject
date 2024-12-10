''''
pip install requests beautifulsoup4 pandas

'''
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL 설정
url = "https://news.naver.com/main/ranking/popularDay.naver"

# HTTP GET 요청
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)

# HTTP 응답 상태 확인
if response.status_code == 200:
    # HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 랭킹 뉴스 제목과 링크 추출
    ranking_news = []
    for news_box in soup.select('.rankingnews_box'):
        media_name = news_box.select_one('.rankingnews_name').get_text(strip=True)
        for news_item in news_box.select('.rankingnews_list .list_content a.list_title'):
            title = news_item.get_text(strip=True)
            link = news_item['href']
            ranking_news.append({"Media": media_name, "Title": title, "Link": link})

    # 데이터프레임 생성
    df = pd.DataFrame(ranking_news)

    # CSV 파일로 저장
    csv_file = "naver_ranking_news.csv"
    df.to_csv(csv_file, index=False, encoding="utf-8-sig")
    print(f"Data exported to {csv_file} successfully!")
else:
    print(f"Failed to retrieve the URL. HTTP Status Code: {response.status_code}")
