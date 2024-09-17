"""
You’re given an array of integers, print the number of times each integer has 
occurred in the array.

Example
Input :
10
1 2 3 3 4 1 4 5 1 2
Output :
1 occurs 3 times
2 occurs 2 times
3 occurs 2 times
4 occurs 2 times
5 occurs 1 times
"""

from collections import Counter

num = int(input())
count = []
sent = ""
for i in range(num):
    sent = sent + input()
count = Counter(sent)

print([f"{key} occurs {value} times" for key, value in count.items()])