#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    val = set([0])
    for i in range(2,n+1):
        val = set([x + a for x in val]) | set([x + b for x in val])
    print(' '.join(map(str, sorted(val))))

if __name__ == '__main__':
    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)
