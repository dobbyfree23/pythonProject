'''
파일명: Ex09-2-built-in-function.py
'''

'''
eval() 함수
    매개변수로 받은 expression(=식)을
    문자열로 받아서 실행하는 함수
'''
expr = input('계산식을 입력하세요 >>> ')
result = eval(expr)
print(f'{expr} = {result}')

'''
divmod() 함수
    두 숫자를 인자로 전달 받아
    첫번째 인자를 두번째 인자로
    나눈 몫과 나머지를 tuple 형식으로 반환
'''
money = 10000
price = 3000
result = divmod(money, price)
print(f'빵을 {result[0]}개 사고 {result[1]}원이 남았다.')



