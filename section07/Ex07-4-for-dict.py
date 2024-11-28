'''
파일명: Ex07-4-for-dict.py

이름	    국어	영어	수학
John	90	85	95
Emily	92	88	96
Michael	98	90	92
Jessica	88	82	78

JSON(JavaScript Object Notation)
'''
students = [
    {'이름': 'John', '국어': 90,'영어': 85,'수학': 95},
    {'이름': 'Emily', '국어': 92,'영어': 88,'수학': 96},
    {'이름': 'Michael', '국어': 98,'영어': 90,'수학': 92},
    {'이름': 'Jessica', '국어': 88,'영어': 82,'수학': 78}
]
'''
세로편집모드 단축키 
Alt + Shift + Ins
'''
for student in students:
    '''
    0: studeunt = {'이름': 'John', '국어': 90,'영어': 85,'수학': 95}
    1: studeunt = {'이름': 'Emily', '국어': 92,'영어': 88,'수학': 96}
    2: studeunt = {'이름': 'Michael', '국어': 98,'영어': 90,'수학': 92}
    3: studeunt = {'이름': 'Jessica', '국어': 88,'영어': 82,'수학': 78}
    
    '''
    print(f'{student['이름']}', end=' ')
    print(f'{student['국어']}', end=' ')
    print(f'{student['영어']}', end=' ')
    print(f'{student['수학']}', end=' ')
    print()


mike = students[2]
for k, v in mike.items():
    print(f'{k}: {v}')


