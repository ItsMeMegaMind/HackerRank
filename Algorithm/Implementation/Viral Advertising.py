#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    out = 0
    a = 5
    a = math.floor(a/2)
    out += a
    for i in range(n-1):
        a*=3
        a = math.floor(a/2)
        out+=a
    return out


if __name__ == '__main__':
    n = int(input())

    result = viralAdvertising(n)

    print(result)
