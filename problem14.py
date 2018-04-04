'''
    The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
    Which starting number, under one million, produces the longest chain?
    NOTE: Once the chain starts the terms are allowed to go above one million.
    Author : thegothamstak
    Date : 4th April 2018
'''
#   To calculate the time taken
import time

#   Start time recorded
start = time.time()

#   Function that accepts a number and returns the collatz value
def calCollatz(number):
    if(number%2 == 0):
        return number/2
    elif(number%2 != 0):
        return  (number * 3) + 1

#   Initializing the 'chain_count' as it will hold the greatest chain throughout the loop
chain_count = 0

#   Loop to find collatz chain counts for all numbers under 1 million
for i in range(2, 1000001):
    count = 0   #   This will store the chain count of all numbers
    num = i     #   Initializing 'num' with i
    #   This loops will calculate collatz as long as 'num' does not reaches the value 1
    while(num > 1):
        num = calCollatz(num)
        count += 1

    #   If the 'count' is greater than the greatest chain count i.e. 'chain_count', 'chain_count = count'
    if(count > chain_count):
        chain_count = count
        chain_num = i   #   Stores the value that has the highest collatz chain

time_taken = time.time() - start

#Prints the value with highest collatz chain
print(str(chain_num)+' has the highest chain of '+str(chain_count))
print('Time taken in seconds is : '+str(time_taken))
