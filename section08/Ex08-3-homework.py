'''
1번
*
**
***
****
*****
******
*******

2번
   *
  **
 ***
****

3번
   *
  ***
 *****
*******

4번

   *
  ***
 *****
*******
 *****
  ***
   *	

'''





i = 0
while i < 7:
    j = 0
    while j < 7:
        if i < 4:
            if j < 3 - i:
                print(" ", end="")
            elif j > 3 + i:
                print(" ", end="")
            else:
                print("*", end="")
        else:
            if j < i - 3:
                print(" ", end="")
            elif j > 9 - i:
                print(" ", end="")
            else:
                print("*", end="")
        j += 1
    print()
    i += 1
