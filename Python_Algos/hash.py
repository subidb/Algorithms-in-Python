class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return "key:{} value:{}".format(self.key, self.value)



class HashTable:

    def __init__(self, capacity = 10):
        self.array = [None]*10
        self.cursize = 0
        self.capacity = capacity


    @staticmethod
    def hash_function(value):
        return value % 10


    def insert(self, key):
        index = self.hash_function(key)
        while self.array[index] is not None:
            index += 1
        node = HashNode(index, key)
        self.array[index] = node


    def search(self, key):
        i = 0
        index = 0
        while i <= self.capacity and self.array[index] is not None:
            index = self.hash_function(key)
            if self.array[index].value == key:
                return index
            i += 1
        return None


table1 = HashTable()


table1.insert(3)
table1.insert(32)
table1.insert(36)
table1.insert(10)
table1.insert(20)
table1.insert(30)
print(table1.array)

print(table1.array[0])

print(table1.search(36))

