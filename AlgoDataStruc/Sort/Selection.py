def sort(array):
    for i in range(0,len(array)):
        smallest = i
        for j in range(i+1,len(array)):
            if array[j]<array[smallest]:
                smallest = j 
                #switch
        tmp = array[i] #Linear
        array[i] = array[smallest] #Linear
        array[smallest] = tmp
        print array
        raw_input()


sort(range(10,0,-1))
