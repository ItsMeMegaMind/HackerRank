#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    l = len(c)
    result = 0
    i = 0
    while(i<l-1):
        if i + 2 < l and c[i + 2] == 0:
            i += 2
            result += 1
        elif i + 1 < l and c[i + 1] == 0:
            i += 1
            result += 1

    return result 


if __name__ == '__main__':
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)