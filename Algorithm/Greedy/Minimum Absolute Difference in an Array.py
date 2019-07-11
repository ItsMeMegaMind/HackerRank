#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

if __name__ == '__main__':


    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr.sort()
    diff = arr[1] - arr[0]

    for i in range(1,n-1):
        diff = min(diff,arr[i+1]-arr[i])
    print(diff)