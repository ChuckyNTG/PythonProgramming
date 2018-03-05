class Node(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n

    @property
    def val(self):
        '''Getter for Val'''
        return self.val
    @val.setter
    def val(self, n):
        '''Setter for Val'''
        self.val = n
    @property
    def next(self):
        '''Getter for next'''
        return self.next
    @next.setter 
    def next(self, n):
        '''Setter for next'''
        self.next = n
        
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x=None):
        self.head = Node(x, None)
        self.sz = 1
        
    def __repr__(self):
        list_links = ''
        link = self.head
        while(link.next):
            print link.next
            list_links += str(link.val) + " -> "
            link = link.next
        list_links += str(link.val)
        return list_links
        
    def isEmpty(self):
        return self.sz == 0
    
    def add(self, n):
        newnode = Node(n)
        self.head.next = self.head = newnode
        self.sz += 1

    def pop(self):
        if self.isEmpty(): return None
        n = self.head
        self.head = self.head.next
        self.sz -=1
        return n
    
    @property
    def sz(self):
        '''Getter for size'''
        return self.sz
    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_num = 0
        l2_num = 0
        l3 = ListObject()
        while( not l1.isEmpty()):
            l1_num += (10 ** l1.sz) * int(l1.pop())
        while( not l2.isEmpty()):
            l2_num += (10 ** l2.sz) * int(l2.pop())
        num_final = l1_num + l2_num
        print list(num_final)

