#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    print(c)
    return max(max([math.floor((c[i + 1] - c[i]) / 2) for i in range(0, len(c) - 1)]),c[0],n-c[-1]-1)


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(result)
