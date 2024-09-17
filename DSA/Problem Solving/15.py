"""
Problem: Determine if one string is a rotation of another.

Input:
String A: "ABCD"
String B: "CDAB"

Output: True

Explanation: B is a rotation of A .
"""
def rotat(str1, str2):
    if len(str1) == len(str2):
        first_ind = str2.find(str1[0])
        str3 = str2[first_ind:] + str2[0:first_ind]
        
        if str3 == str1:
            return True
    return False


str1 = "ABCD"
str2 = "CDAB"
print(rotat(str1,str2))