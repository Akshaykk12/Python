def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(23))

#Time complexity of this code is O(exp(n))