'''
Ex17-2-Exception.py
'''
import traceback

try:
    raise Exception('강제로 발생시킨 예외')
except Exception as e:
    print(f'발생 예외 메시지 {e}')
    traceback.print_exc()