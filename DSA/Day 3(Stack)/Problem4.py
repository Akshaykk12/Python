"""
Balanced Parenthesis
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        curr = self.top
        self.top = self.top.next
        return curr.value
    
    def peek(self):
        return self.top.value
    
    def size(self):
        n = 0
        if self.top == None:
            return 0
        curr = self.top
        while curr != None:
            n+=1
            curr = curr.next
        return n
    
def bal_parant(equ):
     s= Stack()  
     for i in equ:
         if i == "{" or i == "(" or i == "[":
             s.push(i)
         elif i == "}" or i == ")" or i == "]" :
             s.pop()

     if s.size() == 0:
         return "It is a balanced equation"
     else:
         return "It is not a balanced equation"

equation = "{[(a+b)*a]+b}"

print(bal_parant(equation))

