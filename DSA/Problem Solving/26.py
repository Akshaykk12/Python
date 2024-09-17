"""
Problem: Given a string, check if it is a palindrome.
Input:
String: "racecar"
Output: True
Explanation: The string reads the same backward as forward.
"""


def check_palindrome(str1):
    for i in range(int(len(str1)/2)):
        if str1[i] != str1[-(i+1)]:
            return False
    return True

str1 = "racecar"
print(check_palindrome(str1))