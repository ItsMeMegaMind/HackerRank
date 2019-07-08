#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the beautifulDays function below.
if __name__ == '__main__':
    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    out = 0
    for i in range(i, j + 1):
        diff = abs(i - int(str(i)[::-1]))
        out += 1 if diff % k == 0 else 0

    print(out)
