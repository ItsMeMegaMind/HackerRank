#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    c = Counter(arr)
    m = max([i for i in c.values()])
    print(n - m)
