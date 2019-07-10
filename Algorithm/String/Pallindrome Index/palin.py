#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    if len(s)>10e5+5:return -1
    elif isPalin(s) :return -1
    else:
        for i in range(len(s)):
            a = s[:i] + s[i+1:]
            if isPalin(a):
                return i
    return -1

def isPalin(s):
    i = 0
    j = len(s)
    while(i<j//2):
        if (s[i] != s[j-i-1]): return False
        i+=1
        j-=1
    return True

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        print(result)
