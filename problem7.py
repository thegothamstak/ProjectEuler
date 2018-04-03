'''
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10001st prime number?
    Author : thegothamstak
    Date : 3rd April 2018
'''
#Function that will check whether a number is prime or not
def checkPrime(n):
    if(n%2 == 0):
        return False
    i = 3
    while(i < int(n/2) + 1):
        if(n%i == 0):
            return False
        i += 2
    return True

prime_no = 2    #Initializing the 'prime_no' with 2
no = 3          #Initiating the number 'no' with 3 as 'prime_no' is already initialized by 2
prime_count = 1 #Initializing 'prime_count' by 1 as 'prime_no' is already initialzed with the first prime number
#This will increment the 'prime_count' by 1 if the number 'no' is a prime number and store the prime number in 'prime_no'.
while(prime_count < 10001):
    if(checkPrime(no)):
        prime_no = no
        prime_count += 1
        print(str(prime_no)+' at '+str(prime_count))
    no += 2
print('10001st Prime number is : '+str(prime_no))
