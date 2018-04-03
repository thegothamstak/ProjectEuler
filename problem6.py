'''
    The sum of the squares of the first ten natural numbers is,
    12 + 22 + ... + 102 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers
    and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    Author : thegothamstak
    Date : 3rd April 2018
'''
#Function that finds the sum of the squares of the first n natural numbers
def sumSquare(n):
    return int((n * (n + 1) * ((2 * n) + 1))/6)

#Function that finds the square of the sum of the first n natural numbers
def squareSum(n):
    sum = 0
    for i in range(1,n + 1):
        sum = sum + i
    return sum * sum

#Prints the subtraction
print(squareSum(100) - sumSquare(100))
