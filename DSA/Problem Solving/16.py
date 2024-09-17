"""
Problem: Given an array containing n-1 integers in the range from 1 to 
n , find the missing number.

Input:
Array: [1, 2, 4, 5, 6]

Output: 3

Explanation: The missing number is 3
"""

def find_missing(arra):
    for i in range(1,len(arra)+1):
        if i not in arra:
            return i
        
    return 0

arra= [1,2,3,4,5,6]
print(find_missing(arra))