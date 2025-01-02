'''
파일명: Ex25-7-embedding.py

OpenAI 임베딩(Embedding) API - 텍스트의 의미를 벡터로 변환
    텍스트의 의미를 수치화된 벡터로 표현하는 기술
    텍스트 간 유사도 계산, 검색, 분류 등에 활용

    반환되는 백터는 1536 차원
'''
from matplotlib.cbook import silent_list
from openai import OpenAI
import numpy as np

client = OpenAI()

def generate_embedding(text):
    response = client.embeddings.create(
        model='text-embedding-ada-002',
        input=text
    )

    return response.data[0].embedding

def calculate_similarity(embedding1, embedding2):
    '''
    두 임베딩 벡터 간의 코사인 유사도를 계산합니다.
    '''
    return np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))

def find_most_similar(target_text, text_list):

    target_embedding = generate_embedding(target_text)
    similarities = []

    for text in text_list:
        current_embedding = generate_embedding(text)
        similarity = calculate_similarity(target_embedding, current_embedding)
        similarities.append((text, similarity))

    '''
    [
    ('오늘 저녁 뭐 먹지?', 0.91231564xxx),
    ('내일 아침 날씨', 0.91231564xxx),
    ('맛집 추천해주세요',0.8),
    ('운동하는 방법', 0.7)
    ]
    '''

    return max(similarities, key=lambda x: x[1])




# 실행코드
text1 = '오늘 날씨가 좋네요'
text2 = '날씨가 정말 화창하네요'
text3 = '어제 영화를 봤어요'

em1 = generate_embedding(text1)
em2 = generate_embedding(text2)
em3 = generate_embedding(text3)

similarity1 = calculate_similarity(em1, em2)
similarity2 = calculate_similarity(em1, em3)

print(f'"{text1}" 와 "{text2}"의 유사도: {similarity1}' )
print(f'"{text1}" 와 "{text3}"의 유사도: {similarity2}' )

# 예시2

target = '맛있는 저녁 식사'
candidates = [
    '오늘 저녁 뭐 먹지?',
    '내일 아침 날씨',
    '맛집 추천해주세요',
    '운동하는 방법'
]
most_similar_text, similarity_score = find_most_similar(target, candidates)
print(f'"{target}" 와 가장 유사한 문장: {most_similar_text}')
print(f'유사도 점수: {similarity_score}')








