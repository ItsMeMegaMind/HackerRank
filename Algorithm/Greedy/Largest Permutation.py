#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])
    dic = {}
    arr = list(map(int, input().rstrip().split()))
    ind = 0
    for i in arr:
        dic[i] = ind
        ind+=1
    ind = 0
    n = len(arr)

    for i in range(n):
        val = n-i
        if k == 0:
            break
        if arr[i] == val:
            continue
        temp = arr[i]

        ind = dic.get(val)

        arr[i] = val
        arr[ind] = temp
        dic[val] =i
        dic[temp] = ind
        k -= 1
    print( *arr)

