#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    for i in range((len(s) + 1) // 2):
        if s[i] != s[len(s) - i - 1]:
            print(i)
            a = s[:i] + s[i + 1:]
            b = s[:len(s)-i-1]+s[len(s)-i:]
            print(a)
            print(b)
            if isPalin(a):
                return i
            elif isPalin(b):
                return (len(s)-i-1)
    return -1

def isPalin(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]: return False

    return True

if __name__ == '__main__':
    for i in range(int(input())):
        x = input()
        result = palindromeIndex(x)
        print(result)
