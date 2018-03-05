class Tree(object):
    def __init__(self, root):
        self.root = root
        self.size = 1

    def __repr__(self):
        rep = ''
        child = self.root

    def add(self, new_child):
        child = self.root
        while(len(child.children)>=2):
            if child.val<=new_child.val:
                if child.parent:
                    # Add to right if not right child
                    if len(child.parent.children)<2:
                        child = child.parent
                        break
                    else:
                       if child.parent.children[1].val < new_child.val
                           child = child.parent.children[1]
                       else:
                           #swap
                elif child.children[1]:
                    
            else:
                child = child.children[1]
        child.children.append(new_child)

class Child(object):
    def __init__(self, val, parent):
        self.val = val
        self.children = []
        self.parent = parent
   
    def __repr__(self):
        return '{},{}'.format(self.val, self.children)





t = Tree(Child(4,None))
print t.root
t.add(Child(5))
print t.root
t.add(Child(6))
print t.root
t.add(Child(7))
print t.root
t.add(Child(8))
print t.root
t.add(Child(9))
print t.root
t.add(Child(4))
print t.root
