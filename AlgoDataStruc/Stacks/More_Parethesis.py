from stack_01 import Stack

def MoPart(parts):
    s = Stack()
    for i in parts:
        if i in '[({':
            s.push(i)
        else:
            if s.isEmpty():
                print 'Not Balanced'
                return
            else:
                if match(s.pop(),i):
                    continue
                else:
                    print 'Not Balanced'
                    return

    if not s.isEmpty():
        print 'Not Balanced'
    else:
        print 'Balanced'


def match(m1,m2):
    s1,s2 = '[({','])}'
    return s1.index(m1) == s2.index(m2)
    

MoPart(raw_input())
