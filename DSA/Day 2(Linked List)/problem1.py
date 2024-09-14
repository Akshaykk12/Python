"""
Given a LL of characters. Write a program to return a new string that is created by appending all the chars given in LL.

Rules:
-Replace "*" or "/" with single space
-If their are two consecutive "*" or "/" then replace it with single space and covert the next chars in uppercase

Sample Input:
A,n,*,/,a,p,p,l,e,*,a,/,d,a,y,*,*,k,e,e,p,s

Expected Output:
An Apple a day Keeps
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.n = 0

    def append(self, value):

        new_node = Node(value)
        curr = self.head
        if self.head == None:
            self.head = new_node
            self.n += 1
            return

        while curr.next != None:
            curr = curr.next
        
        curr.next = new_node
        self.n += 1

    def __str__(self):

        curr = self.head
        output = ""
        while curr != None:
            output = output + curr.value + "->"
            curr = curr.next

        return output[:-2]
    
    def form_sent(self):
        curr = self.head
        output = ""

        while curr != None:
            if curr.value == "*" or curr.value == "/":
                if curr.next.value == "*" or curr.next.value == "/":
                    curr.next.next.value = curr.next.next.value.upper()
                    curr.next = curr.next.next
                curr.value = " "
            output = output + curr.value
            curr = curr.next
        return output

L= LinkedList()
L.append("A")
L.append("n")
L.append("*")
L.append("/")
L.append("a")
L.append("p")
L.append("p")
L.append("l")
L.append("e")
L.append("*")
L.append("a")
L.append("/")
L.append("d")
L.append("a")
L.append("y")
L.append("/")
L.append("/")
L.append("k")
L.append("e")
L.append("e")
L.append("p")
L.append("s")
print(L)
print(L.form_sent())