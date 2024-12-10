'''
파일명: Ex18-1-requests.py

requests 라이브러리
    HTTP 요청을 보내기 위한 간편하고 인기있는 라이브러리
    이를 사용하여 웹페이지 데이터를 가져오거나,
    API와 상호 작용할 수 있다.

라이브러리 설치 방법
pip install requests

# 라이브러리 설치 에러 발생시
pip install chardet
pip install brotli


URL(Uniform Resource Locator)
    인터넷에서 웹 페이지, 이미지, 동영상 등과 같은 리소스를 찾을수 있는 주소

    ex)https://n.news.naver.com:443/article/003/0012954121?ntype=RANKING

프로토콜(protocol)
    컴퓨터 네트워크를 통해 통신을 수행하기 위한 표준화된 규칙, 절차, 통신 프로세스를 의미

    ex)
        http/https - 웹서버 프로토콜
        ftp - 파일서버 프로토콜
        mailto - 메일 서버 프로토콜
        telnet - 원격지 프로토콜

호스트(host)
    리소스가 위치한 서버의 이름
    ex) n.news.naver.com

포트(Port)
    서버에서 사용하는 방번호
    ex) http - 80, https - 443

경로(Path)
    웹 서버에서 자원에 대한 경로(물리적 또는 추상적 경로)
    ex) /article/003/0012954121

쿼리(Query) - 추가로 서버에 보내는 데이터(parameter)
    ex) ntype=RANKING

'''

import requests
# ?ntype=RANKING
url = 'https://n.news.naver.com/article/003/0012954121'
params = {
    'ntype':'RANKING'
}

response = requests.get(url, params=params)
print(response.text)
