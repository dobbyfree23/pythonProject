'''
파일명: Ex19-1-Linear.py

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
        '''
        linear.insert_data(3, 99)
        self.linear = [3, 5, 4, 99, 2, 6]
        position = 3
        data = 99
        linearSize = 6
        5 ~ 4 -1
        range(5, 3, -1)
         i = 5
         linear[5] = 6
         linear[4] = None
         i = 4
         linear[4] = 2
         linear[3] = None

         linear[3] = 99

        '''
        linear = self.linear

        linear.append(None)
        linearSize = len(linear)

        for i in range(linearSize - 1, position, -1):
            linear[i] = linear[i - 1]
            linear[i - 1] = None

        linear[position] = data


    def delete_data(self, position):
        '''
        self.linear = [3, 5, 99, 2, 6]
        potision = 2
        linear[2] = None
        linearSize = 6

        i = 3 ~ 5
        for i in range(3, 6)
            i = 5
            linear[4] = 6
            linear[5] = None

        del linear[5]
        '''

        linear = self.linear

        linear[position] = None
        linearSize = len(linear)

        for i in range(position+1, linearSize):
            linear[i - 1] = linear[i]
            linear[i] = None

        del linear[linearSize-1]

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

linear.delete_data(2)

linear.print_list()











