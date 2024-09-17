"""
Problem: Given an array of size n , find the majority element (appears more 
than n/2 times).
Input:
Array: [2, 2, 1, 1, 1, 2, 2]
Output:
2
Explanation: The number 2 appears more than n/2 times.
"""

def get_majority_element(arr1):
    arr1.sort()
    unique = set(arr1)
    for i in unique:
        count = arr1.count(i)
        if count > int(len(arr1)/2):
            return i
    return 0

arra= [2, 2, 1, 1, 1, 2, 2]
print(get_majority_element(arra))
