#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the happyLadybugs function below.
def happyLadybugs(b):
    c = Counter(b)
    a = 0
    for i in range(len(b)-1):
        if b[i]!=b[i+1]:
            a=1
            break
    if a==0:return "YES"
    if c['_'] == 0:
        return "NO"
    del c['_']
    for i in c.values():
        if i == 1:
            return "NO"
            break
    return "YES"


if __name__ == '__main__':
    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)
        print(result)
