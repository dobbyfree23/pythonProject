'''
파일명: Ex16-1-constructor-destructor.py

생성자
    객체를 생성할 때 생성자가 자동으로 호출된다.
    주로 객체 초기화 용으로 사용

    생성자 선언방법
        __init__()

소멸자
    인스턴스가 소멸될 때 자동으로 호출된다.

    소멸자 선언방법
        __del__()

'''
import time


class USB:
    def __init__(self, capacity):
        self.capacity = capacity

    def __del__(self):
        print(f'{self.capacity}GB USB를 파기합니다.')


usb1 = USB(128)
print(f'usb1: {usb1.capacity}GB USB 입니다.')

usb2 = USB(1024)
print(f'usb2: {usb2.capacity}GB USB 입니다.')



