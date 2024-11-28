'''
Ex08-2-break.py
'''

i = 0
while i < 7:
    '''
    i=0, 1
    i j = i + 1
    0 *
    1 **
    2 ***
    3 ****
    4 ****
    5 ****
    6 ****
    '''
    j = 0
    while j < i+1:
        print('*', end='')
        if j == 3:
            break
        j += 1
    print()
    i+=1

