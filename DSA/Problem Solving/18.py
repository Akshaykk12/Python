"""
Problem: Given a string, find the length of the longest substring without 
repeating characters.

Input:
String: "abcabcbb"

Output: 3

Explanation: The longest substring is "abc" , which has a length of 3
"""

def long_str(str1):
    output = []
    temp = []
    for i in str1:
        if i not in temp:
            temp.append(i)
        else:
            if len(temp) > len(output):
                output = temp
            temp = []

    return "".join(output)

str1 = "abcabcbb"
print(long_str(str1))