from stack_01 import Stack

def BalancedParenthesis(parths):
    s = Stack()
    for i in parths:
        if "(" in i:
            s.push("(")
        elif ")" in i:    
            if s.isEmpty():
                print 'Not Balanced'
                return
            else:
                s.pop()

    if s.isEmpty():
        print 'Balanced'
    else:
        print 'Not Balanced'



BalancedParenthesis(raw_input())

