'''
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    Author : thegothamstak
    Date : 2nd April 2018
'''
#To calculate the time taken
import time

start = time.time()
sum = 0
for i in range(1000):
    if(i%3 == 0 or i%5 == 0):
        sum = sum + i

time_taken = time.time() - start

print('Sum of all multiples of 3 or 5 below 100 is : '+str(sum))
print('Time taken in seconds : '+str(time_taken))
