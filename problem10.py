'''
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    Author : thegothamstak
    Date : 3rd April 2018

    The code is getting the desired result but takes a lot of time to get it. Working on optimizing the code.
'''
#   To calculate the time taken
import time
start = time.time()

#   Function that will check whether a number is prime or not
def checkPrime(n):
    if(n%2 == 0):
        return False
    if(n > 10):
        if(n%3 == 0):
            return False
        if(n%5 == 0):
            return False
        if(n%7 == 0):
            return False
    i = 3
    while(i < int(n/2) + 1):
        if(n%i == 0):
            return False
        i += 2
    return True

#   Sum of prime numbers below 2 million 'sum_prime', is initialized with 2 as it is the first
#   and the only even prime number.
#   It will be beneficial as the variable 'no' will be iterated by 2 which will result in less iterations.
#   'no' is initialized at 3 as 2 is already considered in 'sum_prime'.

sum_prime = 2
no = 3

while(no < 2000000):
    print(no)
    if(checkPrime(no)):
        sum_prime += no
    no += 2

time_taken = time.time() - start

print('Sum of all Prime numbers below 2 million is : '+str(sum_prime))
print('Time taken in seconds : '+str(time_taken))
