'''
파일명: Ex23-4-matplotlib.py
'''

import random
import matplotlib.pyplot as plt

figure = plt.figure()

axes = figure.add_subplot(121)

axes2 = figure.add_subplot(122)

x = [n for n in range(101)] # [0, 1 ,2, 3 ... , 100] 0부터 100까지 수를 리스트로

y1 = []
y2 = []

for i in range(101):
    y1.append(random.randint(0, 100)) # y1에 0~100 사이의 난수 추가
    y2.append(random.randint(0, 100)) # y2에 0~100 사이의 난수 추가

# 선그래프
axes.plot(x, y1, color='r', marker='.')

axes2.bar(x, y2, color='g')

# 그래프 이미지 저장
plt.savefig('graph.png')

plt.show()
























