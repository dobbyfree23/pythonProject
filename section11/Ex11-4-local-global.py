'''
파일명: Ex11-4-local-global.py

지역변수(Local Variable)
    함수 내부에서 선언된 변수로, 해당 함수 안에서만 사용 가능
    함수가 종료되면 변수는 소멸된다.

전역변수(Global Variable)
    함수 외부에서 선언된 변수로, 프로그램 전체에서 사용 가능
    함수 내부에서도 사용할 수 있지만, 함수 내부에서 변경하려면
    'global' 키워드를 사용해야 한다.

'''

# 전역변수 선언
gVar = '전역'

def globalAndLocal():
    # 지역변수 선언
    lVar = '지역'
    global gVar
    gVar = '변경된 전역'
    print(f'{gVar} 변수입니다.')
    print(f'{lVar} 변수입니다.')

globalAndLocal()
print(gVar)
