'''
파일명: Ex02-6-tuple.py

튜플(Tuple) 
    - 읽기 전용 리스트
    - 수정 불가능 순서가 있는 자료구조
    - 소괄호 () 사용
'''

# 1. 튜플 생성과 기본 조작
game_starter = ('파이리', '이상해씨', '꼬부기')
print('스타터 포켓몬:', game_starter)
print('첫번째 스타터:', game_starter[0])
print('마지막 스타터:', game_starter[-1])
print('전체 스타터 수:', len(game_starter))

# 2. 튜플 슬라이싱
legendary_birds = ('프리져', '썬더', '파이어', '루기아')
print('전설의 새:', legendary_birds[1:3])

# 3. 튜플 수정 불가 테스트
evolve_chain = ('치코타', '베이리프', '메가니움')
''' 튜플 수정 에러발생
evolve_chain[1] = '메가베이리프'
print('튜플 수정 테스트:', evolve_chain)

TypeError: 'tuple' object does not support item assignment
'''
print('evolve_chain 주소값 1:', id(evolve_chain))

# 임시 리스트 변환하여 수정
temp_list = list(evolve_chain)
temp_list[1] = '메가베이리프'
evolve_chain = tuple(temp_list)
print('진화 후:', evolve_chain)
print('evolve_chain 주소값 2:', id(evolve_chain))

# 4. 튜플 언패킹
gym_leader = ('지우', '웅', '로이', '로사')
(leader1, leader2, leader3, leader4) = gym_leader
print('체육관 1번관장:', leader1)
print('체육관 2번관장:', leader2)
print('체육관 3번관장:', leader3)
print('체육관 4번관장:', leader4)

# 5. 튜플 결합
a_team = ('이상해씨', '파이리')
b_team = ('치코리타', '브케인')
c_team = a_team + b_team
print('연합팀:', c_team)





























