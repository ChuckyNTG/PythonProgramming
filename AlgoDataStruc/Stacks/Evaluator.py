from stack_01 import Stack

def Evaluation(express):
    operators = Stack()
    operands = Stack()
    for i in express:
        if i.isdigit():
            operands.push(i)
        elif i in ')':
            n1 = operands.pop()
            n2 = operands.pop()
            o1 = operators.pop()
            operands.push(eval('%s %s %s' % (n1,o1,n2)))
        elif i not in '(':
            operators.push(i)

    print '%d' % (operands.pop()) 


Evaluation(raw_input())
    
