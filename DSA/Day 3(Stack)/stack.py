"""
Stack:-
Node [D]
Stack [D]
Isempty [D]
Pust [D]
Peek [D]
Traverse [D]
Pop [D]
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None
    
    def push(self, value):

        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        if (self.isempty):
            return "Empty Stack"
        else:
            return self.top.value
        
    def pop(self):
        if (self.isempty):
            return "Empty stack"
        else:
            self.top = self.top.next

    def traverse(self):

        curr = self.top
        output = ""
        while curr != None:
            print(curr.value)
            curr = curr.next
        
        return "end"

s = Stack()
print(s.isempty())
s.push(2)
print(s.isempty())
s.push(3) 
print(s.traverse())

# print(s.peek())
s.pop()
print(s.traverse())
