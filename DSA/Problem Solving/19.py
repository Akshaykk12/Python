"""
Problem: Find duplicates in a given array of integers.
Input:
Array: [4, 3, 2, 7, 8, 2, 3, 1]
Output:
Duplicates: 2, 3
"""

def find_dup(arra):
    orig = []
    dub = []
    for i in arra:
        if i not in orig:
            orig.append(i)
        else:
            dub.append(i)
    return dub

arra = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_dup(arra))