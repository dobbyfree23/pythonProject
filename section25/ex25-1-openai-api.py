'''
파일명: ex25-1-openai-api

OpenAI API 사용하기
   OpenAI에서 제공하는 AI(ChatGPT, DALL-E .. 등) 모델을 파이썬에서 활용



pip install openai

'''

from openai import OpenAI

client = OpenAI()

'''
model: 사용할 AI 모델 지정
role: 
    system - AI 지시 또는 역할 부여 (페르소나 지정)
    user - 사용자 

'''
completion = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {
            'role': 'user',
            'content': '이순신 업적 5가지'
         }
    ]
)

print(completion.choices[0].message.content)

'''
이순신(李舜臣)은 조선시대의 유명한 군인으로, 주로 임진왜란(1592-1598) 동안의 업적으로 잘 알려져 있습니다. 그의 주요 업적 5가지는 다음과 같습니다.

1. **명량 해전**: 1597년 명량 해전에서 이순신은 12척의 배로 300척 이상의 일본군 함대를 상대하여 큰 승리를 거두었습니다. 이 전투는 그의 전술적 genius를 잘 보여주는 사례로, 조선 수군의 사기를 높이고 일본의 해상 진출을 저지하는 결정적인 싸움이었습니다.

2. **한산도 해전**: 1592년 한산도 해전에서 그는 일본 수군을 크게 무찌르며 조선 수군의 superiority를 입증했습니다. 이 전투에서 '학익진'이라는 전술을 활용해 일본 함대를 포위하고 대승을 거두었습니다.

3. **거북선 개발 및 운용**: 이순신은 거북선이라는 혁신적인 전투 함선을 발전시키고 이를 전투에 효과적으로 활용했습니다. 거북선은 철갑으로 방호되며, 화포를 장착하여 적 함대에 강력한 화력을 발휘했습니다.

4. **통합 사령부 운영**: 이순신은 조선 수군을 통합하고 조직적으로 운영하여 효율적인 전투 체계를 만들어냈습니다. 그의 뛰어난 지도력 덕분에 다양한 해상 전투에서 승리를 이끌 수 있었습니다.

5. **전쟁 중 정치적 갈등 극복**: 이순신은 전시에도 불구하고 정치적 갈등과 내부의 어려움을 극복하고 군의 통수권자로서 조선 수군을 지휘했습니다. 그의 충성과 헌신은 결국 조선의 해상 방어를 성공적으로 이끌었습니다.

이순신은 전쟁의 영웅일 뿐만 아니라, 그의 전술과 리더십은 한국 역사에서 중요한 부분으로 평가받고 있습니다.

'''

