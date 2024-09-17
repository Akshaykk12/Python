"""
Problem: Rotate an array by k steps to the right.
Input:
Array: [1, 2, 3, 4, 5]
k = 2
Output:
[4, 5, 1, 2, 3]
Explanation: The array is rotated by 2 positions.
"""
def perform_rotat(arr1, k):
    output = []
    leng = len(arr1)  #5
    
    for i in range(k):
        output.append(arr1[leng-k+i])
    for j in range(k+1):
        output.append(arr1[j])
    
    return output

arr1 = [1, 2, 3, 4, 5]
k = 2

print(perform_rotat(arr1, k))