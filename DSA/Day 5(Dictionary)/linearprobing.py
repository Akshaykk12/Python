
class Dictionary:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key ,value):
        hash_value = self.hash_function(key)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value

        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                new_hash_value = self.rehash(hash_value)

                while self.slots[new_hash_value] != None and self.slots[new_hash_value] != key:
                    new_hash_value = self.rehash(new_hash_value)

                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.slots[new_hash_value] = value

                else:
                    self.data[new_hash_value] = value

    def __str__(self):
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                print(self.slots[i], ":", self.data[i], end=" ")

        return ""

    def get(self,key):
        start_pos = self.hash_function(key)
        curr_pos = start_pos

        while self.slots[curr_pos] != None:
            if self.slots[curr_pos] == key:
                return self.data[curr_pos]

            curr_pos = self.rehash(curr_pos)

            if curr_pos == start_pos:
                return "Not Found"
            
        return "Not Found"
    
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def rehash(self, old_hash):
        return old_hash + 1

    def hash_function(self, key):
        return abs(hash(key) % self.size)
    

D1 = Dictionary(3)
print(D1.slots)
print(D1.data)

# D1.put("python", 45)
# print(D1.slots)
# print(D1.data)

# D1.put("Java", 12)
# print(D1.slots)
# print(D1.data)

D1["python"] = 45
D1["java"] = 100
print(D1.slots)
print(D1.data)
print(D1["python"])
print(D1)