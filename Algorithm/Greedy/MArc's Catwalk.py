#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    n = len(calorie)
    calorie.sort(reverse=True)
    out = 0
    for i in range(n):
        calc =  (2**i)*calorie[i]
        out+=calc
    return out


if __name__ == '__main__':

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    print(result)
