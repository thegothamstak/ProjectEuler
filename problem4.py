'''
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    Author : thegothamstak
    Date : 2nd April 2018
'''
#To calculate the time taken
import time

start = time.time()

#Python function that checks whether the number is palindrome
def checkPalindrome(n):
    num = str(n)
    i = 0
    j = len(num) - 1
    while(i <= len(num)/2):
        if(num[i] != num[j]):
            return False
        i = i + 1
        j = j - 1
    return True

largest_palindrome = 0
#This will iterate the 2 numbers from 100 to 999 to check the highest palindrome of their products
for i in range(100,1000):
    for j in range(100,1000):
        if(checkPalindrome(i * j)):
            if(largest_palindrome < i * j):
                largest_palindrome = i * j

time_taken = time.time() - start

print('Largest palindrome made from the product of two 3 digit numbers is : '+str(largest_palindrome))
print('Time taken in seconds : '+str(time_taken))
