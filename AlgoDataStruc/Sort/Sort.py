def Sort(tosort):
    L = tosort.split()
    for i,i_index in enumerate(L):
        for j,j_index in enumerate(L):
            if int(i)<int(j):
                L.insert(i,j_index)
                L.insert(j,i_index)

    return L



Sort(raw_input())
                 
