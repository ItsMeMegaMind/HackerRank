#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    lvl = 0
    out = 0

    for i in s:
        if i == 'U': lvl += 1
        if i == 'D': lvl -= 1
        if i == 'U' and lvl == 0: out += 1
    return out


if __name__ == '__main__':
    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)
