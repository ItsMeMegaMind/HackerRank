#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    nos = math.floor(len(s)/2)+1
    for i in range(1,nos):
        a = s[:i]
        temp = int(a)
        while(len(a)<len(s)):
            temp+=1
            a+=str(temp)
        if a==s:
            return a[:i]


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = separateNumbers(s)
        print(result)
        print("NO" if result == None else "YES " + str(result))