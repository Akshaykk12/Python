"""
What is Linked List?
Node [D]
Create LL [D]
len [D]
insert from head [D]
traverse/ print [D]
insert from tail(append) [D]
insert in middle(after)

clear
delete from head
delete from tail(pop)
delete by value (remove)

search by value(find)
delete by index -> del[0]
search by index (indexing)

"""

class Node:

    def __init__(self, value ):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        #Create an empty linked list
        self.head = None        #empty ll
        self.n = 0              #no. of nodes in ll

    def __len__(self):
        return self.n
    
    def insert_head(self, value):

        #Create  a new node
        new_node = Node(value)

        #create connection
        new_node.next = self.head

        #reassign head
        self.head = new_node

        #increment n
        self.n = self.n + 1

    def __str__(self):
        curr = self.head
        result = ""
        while curr != None:
            result = result + str(curr.value) + "->"
            curr = curr.next
        
        return result[:-2]
    
    def append(self, value):

        new_node = Node(value)
        curr = self.head

        while curr.next != None:
            curr = curr.next
        
        #we are at tail
        curr.next = new_node

# a = Node(1)
# b = Node(34)
# c = Node(29)
# print(a.value)
# print(id(a))
# print(id(b))
# print(id(c))

# a.next = b
# b.next = c                  #here we formed linkedlist manually
# print(a.next)
# print(b.next)
# print(c.next)

# L = LinkedList()
# print(len(L))

L = LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)

print(len(L))
print(L)

L.append(5)
print(L)