#!/bin/python3

import math
import os
import random
import re
import sys



def getWeight(a):
    return (ord(a)- 96)

if __name__ == '__main__':
    s = input()
    out = set()
    prv = ''
    weight = 0
    for curr in s:
        if curr != prv:
            weight = 0
        weight += getWeight(curr)
        out.add(weight)
        prv=curr
    for i in range(int(input())):
        print("Yes" if int(input()) in out else "No")


