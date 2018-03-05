
def start(array):
    sort(array, 0, len(array))

def sort(array, lo, hi):
    #Keep splitting array in half until it is at its base
    if lo>=hi:
       return
    mid = (lo+hi)/2
    sort(array,lo, mid)
    sort(array,mid+1, hi)
    merge(array,lo,hi)
    print array

def merge(array, lo, high):
    #array to take values from
    aux = []
    for k in array:
       aux.append(k) 
    #left array index
    i = lo
    #right array start index
    mid = (lo+high)/2 
    j = mid
    print i,j
    #we want to merge lo to high
    for k in range(lo,high):
        if aux[i]>aux[j]:  
            array[k] = aux[j]
            j+=1
        elif aux[j]>aux[i]:
            array[k] = aux[i]
            i+=1
        elif i>mid:
            array[k] = aux[j]
            j+=1
        elif j>high:
            array[k] = aux[i]
            i+=1


start(range(20,0,-1))
