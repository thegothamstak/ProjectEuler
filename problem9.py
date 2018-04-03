'''
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a2 + b2 = c2
    For example, 32 + 42 = 9 + 16 = 25 = 52.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    Author : thegothamstak
    Date : 3rd April 2018
'''
#To calculate the time taken
import time
start = time.time()

#Function to calculate the pythagorean triplet where a + b + c = 1000 and returns a * b * c
def pytha_triplet():
    for i in range(500):
        for j in range(i + 1, 500):
            for k in range(j + 1, 500):
                if((i * i) + (j * j) == (k * k)):
                    if((i + j + k) == 1000):
                        return (i * j * k)

time_taken = time.time() - start

print('Product of Pythagorean triplet where a+b+c = 1000 is : '+str(pytha_triplet()))
print('Time taken in seconds : '+str(time_taken))
