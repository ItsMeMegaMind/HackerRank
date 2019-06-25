#!/bin/python3
import math
import os
import random
import re
import sys
from itertools import permutations
# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    out = 0
    for i in arr:
        if(((i+d) in arr) and ((i+ 2*d) in arr)):
            out+=1
    return out
if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])
    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(result)