#!/bin/python3

import math

t = int(input())
cycle = int(math.log2((t-1)//3+1))
time = 3*(2**cycle-1)+1
value = 3*2**cycle
print((value-t)+time)

"""
a = int(input())
t=a
dif = 3
n=0
while(t>dif):
    n+=dif
    t-=dif
    dif*=2
print(dif-(a-n)+1)
"""