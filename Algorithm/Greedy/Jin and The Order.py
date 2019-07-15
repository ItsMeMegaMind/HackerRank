#!/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter

if __name__ == '__main__':

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    l = []
    cN = 1
    for i in orders:
        l. append([cN, i[0]+i[1]])
        cN+=1
    l = sorted(l, key=itemgetter(1))
    print(*[i[0] for i in l])

