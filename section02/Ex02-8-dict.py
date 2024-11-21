'''
파일명: Ex02-8-dict.py

딕셔너리(dict)
    - key:value 쌍으로 이루어진 자료구조
    - key는 중복 불가
    - 실제 데이터를 구조화 하는데 유용
'''

# 1. 딕셔너리 생성
pokemon = {
    "name": "피카츄",
    "type": "전기",
    "level": 25,
    "skill": ["백만볼트", "전광석화"]
}
print('포켓몬 정보:', pokemon)

# 접근
print("이름:", pokemon["name"])       # 대괄호 접근
print("타입:", pokemon["type"])
print("레벨:", pokemon.get("level"))  # get() 메서드 접근
print("스킬:", pokemon["skill"][0])

# 2. 딕셔너리 수정
pokemon["level"] = 30       # 값 수정
print("수정 후:", pokemon)
pokemon["speed"] = 5
print("항목 추가:", pokemon)
pokemon.update({"HP": 200})

# 3. 딕셔너리 삭제 메서드
remove_value = pokemon.pop("speed")
print("삭제된 정보:", remove_value)
print("삭제 후:", pokemon)

last_item = pokemon.popitem()   # 마지막 항목 삭제
print("마지막 삭제 항목:", last_item)

# 4. 딕셔너리 메서드
print("모든 키:", type(pokemon.keys()))
print("모든 키:", pokemon.keys())
print("모든 값:", pokemon.values())

print("키 요소1:", list(pokemon.keys())[0])
print("값 요소1:", list(pokemon.values())[0])

print("모든 쌍:", pokemon.items())

# 숙제 이해하기!
print("요소1:", list(pokemon.items())[0][1])








