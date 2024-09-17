"""
Problem: Generate all Pythagorean triplets with values smaller than a given 
limit.

Input: limit = 20
 
Output:
3 4 5
8 6 10
5 12 13
15 8 17
12 16 20

Explanation: The triplets satisfy the condition a² + b² = c² , where a , b , 
and c are integers.
"""

def triplet(limit):
    for a in range(3, limit+1):
        for b in range(a+1, limit+1):
            c_square = a**2 + b**2
            c = int(c_square**0.5)
            if 1< c < limit+1 and c**2 == c_square :
                print (a, b, c)
    return 0


limit = 20
triplet(limit)