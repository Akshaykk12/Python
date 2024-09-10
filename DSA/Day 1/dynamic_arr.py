"""
Dynamic array
1. create List [D]
2. len[D]
3. append [D]
4. print [D]
5. indexing [D]
6. pop [D]
7. clear [D]
8. find [D]
9. insert [D]
10. delete [D]
11. remove [D]
12. sort
13. min
14. max
15. sum
16. extend
17. negative indexing
18. slicing
19. merge

"""

import ctypes
import sys

class MyList:

    def __init__(self):
        self.size = 1
        self.n = 0
        #create a C type array of size = self.size 
        self.A = self.__make_array(self.size) 

    def __len__(self):                                  #this method is important as default len function cannot return length for an object
        return self.n
    
    def __str__(self):                                  #this method returns a string
        result = '' 
        for i in range(self.n):
            result = result + str(self.A[i]) + ","

        return "[" + result[:-1] + "]"
    
    def __getitem__(self, index):
        if 0< index < self.n:
            return self.A[index]
        else:
            return "IndexError - Index out of range"
        
    def __delitem__(self, pos):
        if 0< pos<self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]
            self.n = self.n - 1
    
    def append(self,item):
        if self.size == self.n:
            self.__resize(self.size + 8)
        
        self.A[self.n] = item
        self.n = self.n + 1

    def pop(self):
        if self.n == 0:
            return "Empty list"
        self.n = self.n - 1
        
    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "ValueError: Value not in list"

    def insert(self, pos, item):
        if self.size == self.n:
            self.__resize(self.size + 8)

        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n + 1

    def remove(self, item):
        pos = self.find(item)

        if type(pos) == int:
            self.__delitem__(pos)  
        else:
            return pos

    def __resize(self, new_capacity):
        #create a new array with new capacity
        self.size = self.size + 8
        B = self.__make_array(new_capacity)

        #copy content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        
        #reassign A
        self.A = B

    def __make_array(self, capacity):
        #creates a c type array with size capacity
        return (capacity*ctypes.py_object)()

L = MyList()
print(type(L))
print(L)
print(len(L))

L.append("Hello")
L.append("o")
L.append(84)
L.append(4) 

print(len(L))
print(L)
# print(L[5])
L.pop()
print(L)
# L.clear()
# print(L)
print(L.find(84))
L.insert(0,0)
print(L)

del L[1]
print(L)

L.remove(84)
print(L)