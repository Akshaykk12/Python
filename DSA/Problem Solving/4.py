"""
Write a function to solve the following equation a3 + a2b + 2a2b + 2ab2 +
ab2 + b3.
Write a program to accept three values in order of a, b and c and get the result 
of the above equation
"""
def solve_equ(a,b):
    return (a**3) + (b*(a**2)) + (2*(a**2)*b) + (2*a*(b**2)) + (a*(b**2)) + (b**3)

print(solve_equ(2,4))