def pythago(n):
    count = 0
    for a in range(1,n):
        for b in range(a,n):
            for c in range(b,n+1):
                if a**2 + b**2 == c**2:
                    count+=1


    print count

pythago(141)
 
