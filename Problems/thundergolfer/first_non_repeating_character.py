string = raw_input()
print [i for i in string if string.count(i) == 1][0]
