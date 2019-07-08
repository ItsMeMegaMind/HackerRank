#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    w = list(w)
    i = len(w)
    ans = 0
    for l in (reversed(range(i-1))):
        if(w[l+1]>w[l]):
            pivot = l
            successor = successorCalc(w,l)
            w[pivot],w[successor] = w[successor],w[pivot]
            w = w[:pivot + 1] + [i for i in (reversed(w[pivot + 1:]))]
            return (''.join(w))
        else: pass
    return "no answer"

def successorCalc(w,a):
    pivot = w[a]
    succ = '{'
    index = 0
    for l in (reversed(range(a,len(w)))):
        if w[l]>pivot:
            if(w[l]<succ):
                index=l
                succ = w[l]
    return index


if __name__ == '__main__':

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)
