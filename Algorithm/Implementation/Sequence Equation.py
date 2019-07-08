#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.

if __name__ == '__main__':

    n = int(input())

    p = list(map(int, input().rstrip().split()))
    for i in range(1, n + 1):
        print(p.index(p.index(i) + 1) + 1)

