#!/bin/python3
import math
import os
import random
import re
import sys
from itertools import permutations
# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    perm = permutations(range(len(arr)),3)
    out = 0
    indices = []
    for i in perm:
        if(i[0]<i[1] and i[1]<i[2]):
            indices.append(i)
    for _ in indices:
        i=_[0]
        j=_[1]
        k=_[2]
        if(arr[j]-arr[i]==d and arr[k] - arr[j] ==d):
            out+=1
    return out
if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])
    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(result)

