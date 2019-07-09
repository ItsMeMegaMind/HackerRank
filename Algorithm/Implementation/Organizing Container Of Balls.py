#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    return container


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result)


n = int(input())
a = []
b = []
for i in range(n):
    for j in range(n):
        x = int(input())
        a.append(x)
        b.append(x)
        out = "Possible"

for i in range(n):
    for j in range(i,n):
        if(a[i] == b[j]):
            temp = b[j]
            b[j] = b[i]
            b[i] = temp
            break
    if(j==n):
        out = "Impossible"
        break
print(out)