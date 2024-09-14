"""
Celebrity Problem
""" 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node= Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        curr = self.top
        self.top = self.top.next
        return curr.value

    def size(self):
        n = 0
        curr = self.top
        while curr != None:
            n+=1
            curr = curr.next

        return n

    def traverse(self):
        curr = self.top
        while curr != None:
            print(curr.value)
            curr = curr.next


def find_the_celeb(L):
    s = Stack()
    for i in range(len(L)):
        s.push(i)

    while s.size() >= 2:
        i = s.pop()
        j = s.pop()

        if L[i][j] == 0:
            s.push(i)
        else:
            s.push(j)

    celeb = s.pop()

    for i in range(len(L)):
        if i != celeb:
            if L[i][celeb] == 0 or L[celeb][i] == 1:
                return "There is no celeb"
            
    return celeb
        
L=[
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
]
print(find_the_celeb(L))