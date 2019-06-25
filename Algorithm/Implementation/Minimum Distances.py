#index for index, value in enumerate(l) if value == 1]
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(arr):
    b = set(arr)
    indices = []
    for i in b:
        a = ([index for index, value in enumerate(arr) if value == i])
        if len(a)>1 : indices.append(a)
    if(len(indices)==0): return -1
    else:
        mini = 1e17
        for item in indices:
            b = [item[i+1]-item[i] for i in range(len((item))-1)]
            mini = min(mini,min(b))
        return(mini)
if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(result)
