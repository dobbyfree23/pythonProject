'''
파일명: Ex20-1-Linear.py

자료구조
    데이터를 저장하고 조직화하는 방법론

선형리스트(LinearList)
    간단한 자료구조 중 하나로, 데이터를 일렬로 나열한 것이다.
'''

class LinearList():
    def __init__(self):
        self.linear = []    # 빈 리스트 생성


    # 리스트에 데이터 추가
    def add_data(self, data):
        '''
        self.linear = [3, 5, 4, 2, 6]
        '''
        linear = self.linear
        linear.append(None)
        lLen = len(linear)
        linear[lLen - 1] = data

    # 데이터 삽입
    def insert_data(self, position, data):
        linear = self.linear

        linear.append(None)
        linearSize = len(linear)

        for i in range(linearSize - 1, position, -1):
            linear[i] = linear[i - 1]
            linear[i - 1] = None

        linear[position] = data



    def print_list(self):
        linear = self.linear
        for item in linear:
            print(item)

# 실행코드
linear = LinearList()
linear.add_data(3)
linear.add_data(5)
linear.add_data(4)
linear.add_data(2)
linear.add_data(6)


linear.insert_data(3, 99)


linear.print_list()











