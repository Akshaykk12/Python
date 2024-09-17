"""
Problem: Given a string, find the first character that does not repeat.
Input:
String: "swiss"
Output:
w
Explanation: 'w' is the first character that does not repeat in the string
"""

def get_first_non_repeat(str1):
    for i in range(len(str1)):
        if str1[i] not in str1[i+1:]:
            return str1[i]
    return 0

string="swiss"
print(get_first_non_repeat(string))