num = input()
i=2
while(i**2<num):
    if num % i != 0:
        print True
        break
    i += 1
