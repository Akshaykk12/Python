"""
Problem: Write a function to check if a given number is prime.
Input:
Number: 29
Output: True
Explanation: 29 is a prime number
"""

def check_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
        
    return True

number = 29
print(check_prime(number))