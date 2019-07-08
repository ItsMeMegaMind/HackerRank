#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    b = Counter(a)
    k = b.keys()
    out=[]
    for i in k:
        out.append(b[i]+b[i+1])
    print(max(out))
