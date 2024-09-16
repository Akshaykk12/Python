"""
students are given a string with multiple characters that are repeated 
consecutively. You’re supposed to reduce the size of this string using 
mathematical logic given as in the example below :
Input :
aabbbbeeeeffggg
Output:
a2b4e4f2g3
"""


# def reduce_the_file(sent):
#     Dict = {}
#     for i in sent:
#         if i not in Dict:
#             Dict[i] = 1
#         elif i in Dict:
#             Dict[i] = Dict[i] + 1

#     sent = "".join([f"{key}{value}"for key, value in Dict.items()])
#     return sent

from collections import Counter
def reduce_the_file(sent):
    count = Counter(sent)
    return ''.join([f"{char}{count}" for char, count in count.items()])

nput = "aabbbbeeeeffggg"
print(reduce_the_file(nput))