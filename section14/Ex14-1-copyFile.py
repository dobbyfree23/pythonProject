'''
파일명: Ex14-1-copyFile.py

open 함수 모드
    b(binary mode): 해당 파일의 데이터를 바이너리 파일로 인식하고 입출력
'''

buffer_size = 1024
with open('../section13/hello.txt', 'rb') as org_file:
    with open('hello2.txt', 'wb') as copy_file:
        while True:
            buffer = org_file.read(buffer_size)
            if not buffer:
                break
            copy_file.write(buffer)

print('hello2.txt 파일이 복사되었습니다.')









