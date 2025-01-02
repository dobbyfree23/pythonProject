'''
파일명: Ex25-3-openai-image-generation.py

DALL-E 3 API - 이미지 생성하기
    OpenAI의 DALL-E 3 모델을 사용하여 텍스트 설명(프롬프트)으로
    이미지 생성하기
'''

from openai import OpenAI
import time

client = OpenAI()

def generate_image(prompt, size='1024x1024', quality='standard', n=1):

    response = client.images.generate(
        model='dall-e-3',
        prompt=prompt,
        size=size,
        quality=quality,
        n=n
    )
    return response.data[0].url


# 실행코드
# prompt1 = '한국의 전통 한옥과 현대적 고층 빌딩이 조화롭게 아우러진 도시 풍경'
# result1 = generate_image(prompt1)
# print(f'기본 이미지 생성 결과: {result1}')


prompt2 = '벚꽃이 만발한 경북궁의 봄 풍경'
result2 = generate_image(
    prompt2,
    size='1024x1792',
    quality='hd'
)
print(f'프롬프트2: {result2}')


# prompt3 = '제주도의 푸른 바다와 오름이 있는 자연 풍경'
# result3 = generate_image(
#     prompt3,
#     size='1792x1024',
#     quality='standard'
# )
# print(f'프롬프트3: {result3}')



