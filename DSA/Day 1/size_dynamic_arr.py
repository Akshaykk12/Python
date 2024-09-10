import sys

L=[]
print(sys.getsizeof(L))

L.append("Hello")
print(sys.getsizeof(L))

L.append("Hi")
print(sys.getsizeof(L))

L.append("How")
print(sys.getsizeof(L))

L.append("Are")
print(sys.getsizeof(L))

L.append("You")
print(sys.getsizeof(L))

L.append("?")
print(sys.getsizeof(L))

L=[]
for i in range(100):
    print(i, sys.getsizeof(L))
    L.append(i)