def sort(array):
    change = 1
    while(change != 0):
        change = 0
        for i in range(0,len(array)-1):
            if array[i]>array[i+1]:
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp
                change += 1
                print array
                raw_input()

sort(list('sortexample'))
