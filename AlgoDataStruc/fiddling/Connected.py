class Component(object):
    def __init__(self, val=None, connection=None):
         self._val = val
         self._connection = connection

    def __repr__(self):
        return '({},{})'.format(self._val,self._connection) 

    @property
    def val(self):
        ''' Getter for val.'''
        return self._val

    @property
    def connection(self):
        '''Getter for connection.'''
        return self._connection

    @connection.setter
    def connection(self, num):
        self._connection = num

class Mapping(object):
    def __init__(self, size):
        self.size = size
        self.map = [Component(num,num) for num in range(size)]

    def __repr__(self):
        return '{}'.format(self.map)

    def connected(self, p, q):
        return self.map[p].val == self.map[q].val

    def union(self, p, q):
        if self.connected(p,q):
            return
        for comp in self.map:
            if comp.connection == self.map[q].connection:
                comp.connection = self.map[p].connection 

    def connections(self):
        conns = {} 
        for comp in self.map:
            if comp.connection not in conns.keys():
                conns[comp.connection] = [comp.val]
            else:
                conns[comp.connection].append(comp.val)
        return conns
