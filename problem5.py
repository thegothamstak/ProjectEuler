'''
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    Author : thegothamstak
    Date : 3rd April 2018

    The code is getting the desired result but takes a lot of time to get it. Working on optimizing the code.
'''
def checkDivisible(n):
    for i in range(1,21):
        if(n%i != 0):
            return False
    return True

div = 1
while(True):
    print(div)
    if(checkDivisible(div)):
        print(div)
        break
    else:
        div = div + 1
