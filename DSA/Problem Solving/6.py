"""
Bela teaches her daughter to find the factors of a given number. When she 
provides a number to her daughter, she should tell the factors of that number. 
Help her to do this, by writing a program.
Note :
If the input provided is negative, ignore the sign and provide the output. If 
the input is zero
If the input is zero the output should be “No Factors”.
Sample Input 1:
54
Sample Output 1:
1, 2, 3, 6, 9, 18, 27, 54
"""

def find_fact(num):
    output = []
    for i in range(1, num+1):
        if (num % i) == 0:
            output.append(i)

    return output

num = int(input())
print(find_fact(num))