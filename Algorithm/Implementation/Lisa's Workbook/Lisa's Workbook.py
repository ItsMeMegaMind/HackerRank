#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    out = 0
    now = 1
    list1=[]
    totalPage=0
    for i in range(len(arr)):
        problems = arr[i]
        temp=0
       # if problems>k:
        firstPage,secondPage = divmod(problems,k)
        totalPage += firstPage+ (1 if secondPage else 0)
        for j in range(firstPage):
            a = [i for i in range(j*k+1,(j+1)*k+1)]
            list1.append(a)
            now+=1
            temp = a[len(a)-1]
        if(secondPage):
            list1.append([i for i in range(temp+1,temp+secondPage+1)])
            now+=1
    #print(list1)

    for i in range(len(list1)):
        if i+1 in list1[i]:
            out+=1

    return(out)


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    print(result)