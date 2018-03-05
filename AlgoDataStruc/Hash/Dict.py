from sll import SinglyLinkedList

class dict(object):

    def __init__(self):
        self.keys = self.data = self.table = [None] * 13

    def __getitem__(self, key):
        return hashfun(key)
        
    def hashfun(self, key):
        divisor = ''
        for char in key:
            divisor += ord(char)
        return divisor % 13

    def put(self, key, data):
        val = hashfun(key)
        if self.table[val]:
            old_data = self.table[val]
            self.table[val] = data
            self.data.remove(old_data)
            self.data.append(data)
