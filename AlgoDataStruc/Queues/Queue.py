class Node(object):

    def __init__(self, val=None, n=None):
        self.__item = val
        self.__nextnode = n

    def __repr__(self):
        return '{}({!r},{!r})'.format(
            self.__class__.__name__,
            self.__item, self.__nextnode)

    @property
    def item(self):
        """Return the item."""
        return self.__item

    @property
    def nextnode(self):
        """Return the nextnode."""
        return self.__nextnode

    @nextnode.setter
    def nextnode(self, n):
        """Set the nextnode."""
        self.__nextnode = n


class Queue(object):

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__sz = 0

    @property
    def sz(self):
        return self.__sz

    def is_empty(self):
        return self.__sz == 0

    def enqueue(self, item):
        n = Node(item, None)
        if self.is_empty():
            self.__head = self.__tail = n
        else:
            self.__tail.nextnode = self.__tail = n
        self.sz += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Empty!")
        else:
            n = self.__head
            self.__head = self.__head.nextnode
            self.sz -= 1
            return n.item
