"""
Queue
Node [D]
Queue [D]
Enqueue [D]
Dequeue [D]
Traverse [D]
Empty [D]
Size [D]
Front Item [D]
Rear Item [D]
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.front and self.rear == None:
            self.front, self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):

        if self.front == None:
            return "Empty Queue"
        else:
            self.front = self.front.next

    def is_empty(self):
        self.front = None

    def size(self):
        curr = self.front
        counter = 0
        while curr != None:
            counter += 1
            curr = curr.next
        return counter

    def traverse(self):
        curr = self.front
        while curr != None:
            print(curr.value)
            curr = curr.next

    def front_item(self):
        if self.front == None:
            return "Empty"
        return self.front.vale

    def rearr_item(self):
        if self.rear == None:
            return "Empty"
        return self.rear.vale
