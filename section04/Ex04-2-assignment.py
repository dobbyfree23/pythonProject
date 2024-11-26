'''
파일명: Ex04-2-assignment.py

대입 연산자
    변수에 값을 할당하는 연산자
    단순 대입: (=)

복합 대입 연산자
    연산과 할당을 동시에 수행하는 복합 연산자
    (+=, -=, *=, /=, %=)
'''
# 1. 기본 대입
pokemon = '피카츄'
level = 25
print(f'포케몬: {pokemon}, 레벨: {level}')

# 2. 다중 대입과 교환
hp, mp = 100, 50
print(f'체력: {hp}, 마나: {mp}')

hp, mp = mp, hp     # 값 교환
print(f'교환 후- 체력: {hp}, 마나: {mp}')

# 임시변수 사용 교환
tmp = hp
hp = mp
mp = tmp
print(f'tmp 사용 교환 후- 체력: {hp}, 마나: {mp}')

# 3. 복합 대입
exp = 0
exp += 50   # exp = exp + 50
            # 50의 경험치 획득
print(f'경험치 획득: {exp}')












