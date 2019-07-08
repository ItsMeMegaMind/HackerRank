#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    n=0
    while(s>=p):
        s-=p
        n+=1
        if(p>m+d): p-=d
        else: p=m
    return n

if __name__ == '__main__':

    pdms = input().split(" ")

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    print(answer)