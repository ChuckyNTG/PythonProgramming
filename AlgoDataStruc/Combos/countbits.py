
def countBits(num):
    def count(i):
        if (i<=0):
            return 0
        else:
            mod = i % 2
            return mod + count(i//2)
    return [count(i) for i in range(num +1)]


print(countBits(5))

