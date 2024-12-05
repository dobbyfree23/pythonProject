'''
Ex12-99-practice.py
'''

import random
import time

pot = [n for n in range(1, 46)]

jackpot = []

for n in range(1, 7):
    random.shuffle(pot)

    pick = pot.pop()
    print(f'{n}번째 번호는 {pick} 입니다.')
    jackpot.append(pick)
    time.sleep(1)

jackpot.sort()
print(jackpot)
