"""
What is Linked List?
Node [D]
Create LL [D]
len [D]
insert from head [D]
traverse/ print [D]
insert from tail(append) [D]
insert in middle(after) [D]

clear [D]
delete from head [D]
delete from tail(pop) [D]
delete by value (remove) [D]

search by value(find) [D]
delete by index -> del[0] []
search by index (indexing) [D]

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

        if self.head == None:
            #empty list
            self.head = new_node
            self.n = self.n + 1
            return

        curr = self.head

        while curr.next != None:
            curr = curr.next
        
        #we are at tail
        curr.next = new_node

        self.n = self.n + 1

    def insert_after(self, after, value):

        new_node = Node(value)

        curr = self.head
        while curr != None:
            if curr.value == after:
                break
            curr = curr.next

        #found after valur
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1

        #after value not found
        else:
            return "Item not found"
        
    def clear(self):
        self.head = None
        self.n = 0

    def del_head(self):
        if self.head == None:
            return "Empty LL"
        
        self.head = self.head.next
        self.n = self.n - 1

    def pop(self):

        if self.head == None:
            return "LL is already empty"

        curr = self.head

        if curr.next == None:
            return self.del_head()

        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n = self.n - 1

    def remove(self, value):

        curr = self.head

        if curr == None:
            return "Empty LL"

        if curr.value == value:
            return self.del_head
        
        while curr.next != None:
            if curr.next.value == value:
                break
            curr = curr.next

        if curr.next == None:
            return "Item not found"
        else:
            curr.next = curr.next.next
            self.n = self.n - 1

    def search(self, value):

        pos = 0
        curr = self.head

        if self.head == None:
            return "Empty LL"
        

        while curr.next != None:
            if curr.value == value:
                return pos
            curr = curr.next
            pos += 1

        return "Item not found"
    
    def del_by_ind(self, pos):
        ind = 0
        curr = self.head

        while curr.next != None:
            if ind == pos:
                return self.remove(curr.value)
            curr = curr.next
            ind += 1

        return "IndexError"

    def __getitem__(self, pos):
        ind = 0
        curr = self.head
        

        while curr.next != None:
            if pos == ind:
                return curr.value
            curr = curr.next
            ind += 1

        return "IndexError"

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
print(len(L))
L.insert_after(3,100)
print(L)
# L.clear()
# print(L, len(L))
L.del_head()
print(L)
L.pop()
print(L)
L.remove(200)
print(L, len(L))
print(L.search(100))
L.del_by_ind(2)
print(L)
print(L[1])