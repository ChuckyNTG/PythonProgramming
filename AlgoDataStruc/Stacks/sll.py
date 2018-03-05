class Node(object):

    def __init__(self, val=None, n=None):
        self._item = val
        self._nextnode = n

    def __del__(self):
        print 'Node Dead: {!s}'.format(self._item)

    def __repr__(self):
        return '{}({!r}, {!r})'.format(
            self.__class__.__name__,
            self._item, self._nextnode)

    @property
    def item(self):
        """Get the item."""
        return self._item

    @property
    def nextnode(self):
        """Get the next node."""
        return self._nextnode

    @nextnode.setter
    def nextnode(self, n):
        self._nextnode = n


class SinglyLinkedList(object):

    def __init__(self):
        self._head = None
        self._tail = None
        self._sz = 0

    def __repr__(self):
        n = self._head
        linklist = ""
        while n:
            linklist += n.__repr__() + '=>'
            n = n.nextnode
        return linklist

    def is_empty(self):
        return self._sz == 0

    @property
    def sz(self):
        """Get the size."""
        return self._sz

    def insert(self, item):
        n = Node(item)
        if self.is_empty():
            self._head = self._tail = n
        else:
            n.nextnode = self._head
            self._head = n

        self._sz += 1

    def remove(self):
        if self.is_empty():
            raise IndexError("List is Empty")
        else:
            self._head = self._head.nextnode

        self._sz -= 1
