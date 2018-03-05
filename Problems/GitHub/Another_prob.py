n = input()
lookup = [-1] * (n+1)
def fib(num):
    if num == 0:
        lookup[num] = 0
    elif num == 1:
        lookup[num] = 1
    elif lookup[num] == -1:
        lookup[num] = fib(num-1) + fib(num-2)
    return lookup[num]


fib(n)
print ','.join(map(str,lookup))
