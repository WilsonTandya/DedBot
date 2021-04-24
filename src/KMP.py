def KMP(pat, txt):
    M = len(pat)
    N = len(txt)

    borderfunction = [0 for i in range (M-1)]
    j = 0
  
    a = 0
    b = 1
    while (b < M-1):
        if pat[b]== pat[a]:
            a += 1
            borderfunction[b] = a
            b += 1
        else:
            if a != 0:
                a = borderfunction[a-1]
            else:
                borderfunction[b] = 0
                b += 1
    print(borderfunction)
  
    i = 0 
    while (i < N):
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if (j == M):
            print ("Ditemukan pada indeks ke- "+ str(i-j))
            j = borderfunction[j-2]
        elif (i < N and pat[j] != txt[i]):
            if j != 0:
                j = borderfunction[j-1]
            else:
                i += 1

'''
txt = "AAACAAACAAAA"
pat = "AAACAAAA"
KMP(pat, txt)'''