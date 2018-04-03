'''
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    Author : thegothamstak
    Date : 2nd April 2018

    The code is getting the desired result but takes a lot of time to get it. Working on optimizing the code.
'''
#To calculate the time taken
import time

start = time.time()

#Function to check whether a number is prime number or not
def checkPrime(n):
    if(n%2 == 0):
        return False
    i = 3
    while(i < int(n/2) + 1):
        if(n%i == 0):
            return False
        i += 2
    return True

no = 3
prime_no = 2
while(no < int(600851475143/2) + 1):
    #print(no)
    #Checked if the number is a factor of 600851475143 and is a prime number
    if(600851475143%no == 0):
        if(checkPrime(no)):
            #print(no)
            prime_no = no
    no += 2

time_taken = time.time() - start

print('Largest prime factor of the number 600851475143 : '+str(prime_no))
print('Time taken in seconds : '+str(time_taken))
