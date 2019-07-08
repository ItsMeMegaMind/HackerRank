#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))
    a_final = [None]*n
    for i in range(n):
        a_final[(i+k)%n] = a[i]
    queries = []

    for _ in range(q):
        print(a_final[int(input())])




