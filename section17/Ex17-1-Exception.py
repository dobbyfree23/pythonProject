'''
파일: Ex17-1-Exception.py

예외(Exception)
    프로그램 실행중 발생할 수 있는 오류나 예기치 않은 상황
'''

try:
    print('서버에 접속 합니다.')
    a = int(input('제수를 입력하세요>>> '))
    b = int(input('피제수를 입력하세요>>> '))

    print(f'a/b : {a / b}')
except ValueError:
    print('정수만 입력할 수 있습니다.')
except ZeroDivisionError:
    print('0으로 나누는 것은 불가능합니다.')
except:
    print('예외가 발생했습니다.')
else:   # 예외가 발생하지 않으면 처리되는 영역
    print('정상종료!')
finally:
    print('서버 접속 종료합니다.')
