from stack_01 import Stack
from test import testEqual

def revstring(mystr):
    s = Stack()
    revstr = ''
    for i in mystr:
        s.push(i)

    while not s.isEmpty():
        revstr += s.pop()

    return revstr
  


testEqual(revstring('apple'),'elppa')
