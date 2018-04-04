'''
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2^1000?
    Author : thegothamstak
    Date : 4th April 2018
'''
#   To calculate the time taken
import time

#   Start time recorded
start = time.time()

#   Calculating 2 ^ 1000
power_val = 2 ** 1000

#   Initializing 'sum_val' to 0 as it will hold the sum of all the digits of 'power_val'
sum_val = 0
#   Calculating 'sum_val' by traversing through each digit of 'power_val' as a String
for i in range(len(str(power_val))):
    sum_val += int(str(power_val)[i])

time_taken = time.time() - start

#   Printing the sum of all the digits of 2 ^ 1000
print('The sum of the digits of 2 ^ 1000 is : '+str(sum_val))
