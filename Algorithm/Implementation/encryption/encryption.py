#!/bin/python3

import math
def encryption(s):
    s = s.replace(" ", "")
    n = len(s)
    l = math.sqrt(n)
    r,c = math.ceil(l),math.floor(l)
    print(r,c)
    if(r*c<n): c+=1
    arr = [list(s[i:i+r]) for i in range(0,len(s),r)]
    print(arr)
    out = ""
    for i in range(r):
        try:
            for j in range(c):
                out += (arr[j][i])
            out+=" "
        except IndexError:
            out+=" "
            pass
    return(out)
s = input()
print(encryption(s))

