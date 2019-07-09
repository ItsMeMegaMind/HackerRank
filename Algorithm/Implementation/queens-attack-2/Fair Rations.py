#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the fairRations function below.
def fairRations(B):
    out = 0
    if sum(B) % 2 != 0:
        return "NO"
    else:
        for i in range(len(B) - 1):
            if B[i] % 2 != 0:
                B[i] += 1
                B[i + 1] += 1
                out += 2
        if B[len(B) - 1] % 2 == 0:
            return (out)
        else:
            return "NO"


if __name__ == '__main__':
    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)
    print(result)