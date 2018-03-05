class _Node(object):

    def __init__(self,data=None,node=None):
        self.data = data
        self.node = node
      
    def get_data(self):
        return self.data
  
    def get_next(self):
        return self.node
 
    def set_next(self,n):
        self.node = n

class Stack(object):
    
    def __init__(self,head=None):
        self.head = head
        self.size = 0

    def Size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self,item):
        link = None
        if self.head:
            link = self.head
        self.head = _Node(item,link)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return None
        item = self.head.get_data()
        self.head = self.head.get_next()
        self.size -= 1
        return item
        
        

            
    
        
