#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        a = list(map(int, input().rstrip().split()))
        print(min([width[i] for i in range(a[0], a[1] + 1)]))
