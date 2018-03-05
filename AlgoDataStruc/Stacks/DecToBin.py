from stack_01 import Stack

s = Stack()
def DecBin(dec):
    if dec<1:
        binar = []
        while not s.isEmpty():
           binar.append(str(s.pop())) 
        print ''.join(binar)
        return
    s.push(dec % 2)
    return DecBin(dec/2)

DecBin(int(raw_input()))

