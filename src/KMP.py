def KMP(path, txt):
    #Buat borderfunction dari pattern
    borderfunction = [0 for i in range (len(path)-1)]
  
    a = 0
    b = 1
    while (b < len(path)-1):
        if path[b]== path[a]:
            a += 1
            borderfunction[b] = a
            b += 1
        else:
            if a != 0:
                a = borderfunction[a-1]
            else:
                borderfunction[b] = 0
                b += 1

    i = 0 
    j = 0
    while (i < len(txt)):
        if path[j] == txt[i]:
            i += 1
            j += 1
        if (j == len(path)):
            return True
        elif (i < len(txt) and path[j] != txt[i]):
            if j != 0:
                j = borderfunction[j-1]
            else:
                i += 1
    return False