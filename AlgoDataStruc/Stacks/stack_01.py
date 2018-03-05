class Stack():
    def __init__(self):
        self.contents = []
    def size(self):
        return len(self.contents)
    def isEmpty(self):
        return self.size() == 0
    def push(self,i):
        self.contents.append(i)
    def pop(self):
        return self.contents.pop() 
