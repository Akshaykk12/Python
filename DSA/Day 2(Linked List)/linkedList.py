"""
What is Linked List?
Node [D]
Create LL
len
insert from head
traverse/ print
insert from tail(append)
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

a = Node(1)
b = Node(34)
c = Node(29)
print(a.value)
print(id(a))
print(id(b))
print(id(c))

a.next = b
b.next = c                  #here we formed linkedlist manually
print(a.next)
print(b.next)
print(c.next)