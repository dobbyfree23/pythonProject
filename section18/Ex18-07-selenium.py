"""
파일명: Ex18-06-selenium.py

selenium 패키지
    어플리케이션 테스트하기 위한 프레임웍
    웹 어플리케이션 다양한 브라우저 동작 테스트용!
    크롤링으로 많이 사용된다

패키지 설치
    pip install selenium
    pip install webdriver-manager

** 패키지설치 에러시 **
    visual studio build tools 설치 >> C++ 빌드 설치
"""

import os
import time
import urllib.request

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

def scroll_and_load_images(driver, target_count):
    """스크롤을 통해 충분한 수의 이미지를 로드하는 함수"""

    last_height = driver.execute_script("return document.body.scrollHeight")
    loaded_images = 0

    while loaded_images < target_count:
        # 페이지 끝까지 스크롤
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 페이지가 로드될 시간 대기
        time.sleep(2)

        # 현재 로드된 이미지 개수 확인
        thumbnails = driver.find_elements(By.CSS_SELECTOR, '.H8Rx8c')
        loaded_images = len(thumbnails)

        print(f"현재 로드된 이미지 수: {loaded_images}")

        # 새로운 높이 확인
        new_height = driver.execute_script("return document.body.scrollHeight")

        # "결과 더보기" 버튼이 있는지 확인하고 클릭
        try:
            show_more_button = driver.find_element(By.CSS_SELECTOR, '.YstHxe input[type="button"]')
            if show_more_button.is_displayed():
                driver.execute_script("arguments[0].click();", show_more_button)
                print("'결과 더보기' 버튼 클릭")
                time.sleep(3)
                continue
        except NoSuchElementException:
            pass

        # 더 이상 로드할 이미지가 없으면 종료
        if new_height == last_height:
            print("더 이상 로드할 이미지가 없습니다.")
            break

        last_height = new_height

        # 무한 루프 방지를 위한 최대 시도 횟수 제한
        if loaded_images > target_count * 3:  # 목표의 3배까지만 시도
            break

    return driver.find_elements(By.CSS_SELECTOR, '.H8Rx8c')

def download_images(keyword, num_images=10, output_dir='images'):

    # Chrome driver 자동 설치 및 서비스 생성
    service = Service(ChromeDriverManager().install())

    # Chrome 옵션 설정 (선택사항)
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Chrome 드라이버 인스턴스 생성
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # 드라이버를 통해 Google 페이지 접속
        driver.get('https://images.google.com/')

        # 검색어 입력
        search_bar = driver.find_element(By.NAME, 'q')
        search_bar.send_keys(keyword)
        search_bar.send_keys(Keys.RETURN)

        # 출력 디렉토리 생성
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 초기 로딩 대기
        time.sleep(3)

        # 스크롤을 통해 충분한 이미지 로드
        print(f"'{keyword}' 검색 결과에서 {num_images}개의 이미지를 찾는 중...")
        thumbnails = scroll_and_load_images(driver, num_images)

        print(f"총 {len(thumbnails)}개의 이미지를 찾았습니다.")

        # 이미지 다운로드
        downloaded_count = 0

        for idx, thumbnail in enumerate(thumbnails[:num_images]):
            if downloaded_count >= num_images:
                break

            try:
                # 썸네일 클릭
                driver.execute_script("arguments[0].click();", thumbnail)
                time.sleep(2)

                # 큰 이미지 로드 대기
                image = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '.sFlh5c.FyHeAf.iPVvYb')
                    )
                )

            except TimeoutException:
                print(f'{idx+1}번째 이미지 로드 실패 - 건너뜀')
                continue
            except Exception as e:
                print(f'{idx+1}번째 이미지에서 알 수 없는 에러: {e}')
                continue

            # 이미지 URL 가져오기
            image_url = image.get_attribute('src')

            # data: URL은 건너뜀
            if image_url.startswith('data:'):
                print(f'{idx+1}번째 이미지는 data URL - 건너뜀')
                continue

            print(f'{idx+1}번째 이미지 URL: {image_url}')

            # 확장자 확인
            check_ext = ['jpg', 'jpeg', 'png', 'gif', 'webp']

            try:
                ext = image_url.split('.')[-1].split('?')[0].lower()
                if ext not in check_ext:
                    print(f'{idx+1}번째 이미지는 지원하지 않는 확장자 ({ext}) - 건너뜀')
                    continue
            except:
                ext = 'jpg'  # 기본 확장자

            # 이미지 다운로드
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                request = urllib.request.Request(image_url, headers=headers)

                with urllib.request.urlopen(request, timeout=10) as response:
                    filename = f'{output_dir}/{keyword}_{downloaded_count+1}.{ext}'
                    with open(filename, 'wb') as file:
                        file.write(response.read())

                    downloaded_count += 1
                    print(f'{downloaded_count}번째 이미지 다운로드 완료: {filename}')

            except Exception as e:
                print(f'{idx+1}번째 이미지 다운로드 실패: {e}')
                continue

        print(f'\n다운로드 완료! 총 {downloaded_count}개의 이미지가 {output_dir} 폴더에 저장되었습니다.')

    finally:
        # 드라이버 종료
        time.sleep(2)
        driver.quit()

# 실행코드
if __name__ == "__main__":
    keyword = '차은우'
    num_images = 50000  # 더 많은 이미지를 테스트해볼 수 있도록 증가
    output_dir = 'images'

    # 이미지 다운로드 함수 호출
    download_images(keyword, num_images, output_dir)