'''
파일명: Ex23-2-matplotlib.py
'''
from cProfile import label

import matplotlib.pyplot as plt

# Figure와 Axes 객체 동시생성
fig, ax = plt.subplots()


# 데이터 설정
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange'] # 각 막대의 색상

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')

ax.set_title('Fruit supply by kind and color')

ax.legend(title='Fruit color')

plt.show()






















