'''
파일명: Ex14-3-csvWriter.py
'''

import csv

with open('차량관리.csv', 'w', newline='',encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',', quotechar='"')
    csv_maker.writerow([1, '08러1234', '2024-12-05,21:43'])
    csv_maker.writerow([2, '08러5678', '2024-12-03,21:43'])
    csv_maker.writerow([3, '02나4567', '2024-12-02,21:43'])

print('차량관리.csv 파일이 생성되었습니다.')
