"""
String Reversal: Reverse a string
"""

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def add(self, stri):

        for i in stri:
            new_node = Node(i)
            new_node.next = self.top
            self.top = new_node
            


    def __str__(self):
        curr = self.top
        output = ""
        while curr != None:
            output = output + curr.value
            curr = curr.next
        
        return output
    
s = Stack()
s.add("Hello")
print(s)
