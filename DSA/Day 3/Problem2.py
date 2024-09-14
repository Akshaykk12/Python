"""
Undo-Redo Problem

Input = Hello
        uuur
Output = Hel 
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
        if self.top == None:
            return "String is Empty"
        else:
            self.top = self.top.next
    
    def peek(self):
        if self.top == None:
            return "Empty String"
        else:
            return self.top.value
        
    def __str__(self):
        curr = self.top
        output = ""
        while curr != None:
            output += curr.value
            curr = curr.next
        return output[::-1]


def undo_redo(text, cond):
    s = Stack()
    for i in text:
        s.push(i)
    last = ""
    for j in cond:
        if j == "u":
            last = s.peek()
            s.pop()
        else:
            if last == "":
                pass
            else:
                s.push(last)

    return s
    
text = "Hello"
cond = "uuur"
print(undo_redo(text, cond))
    

