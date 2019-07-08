#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []
    right = 0
    left = n+1
    down = 0
    up = n+1
    leftUp =1
    rightUp = n+1
    leftDown = 0
    rightDown = 0

    for _ in range(k):
        obstacle = (list(map(int, input().rstrip().split())))
        if(obstacle[0] ==r_q):
            if(obstacle[1]>c_q):
                left = min(obstacle[1],left)
            else:
                right = max(obstacle[1],right)
        elif (obstacle[1] ==c_q):
            if(obstacle[0]>r_q):
                up = min(obstacle[0],up)
            else:
                down = max(obstacle[0],down)
        elif((abs(obstacle[0]-r_q)==abs(obstacle[1]-c_q))):
            if(obstacle[1] <c_q): #left
                if (obstacle[0] > r_q): #up
                    leftUp = min(leftUp,obstacle[0])
                else:
                    leftDown = max(leftDown,obstacle[0])
            else:
                if (obstacle[0] > r_q): #up
                    rightUpUp = min(rightUp,obstacle[0])
                else:
                    rightDown = max(rightDown,obstacle[0])

    print(right)
    print(left)
    print(up)
    print(down)
    print(leftUp)
    print(leftDown)
    print(rightDown)
    print(rightUp)
    result =   abs(right - r_q ) -1
    result += abs(r_q - left ) -1
    result += abs( up - c_q ) -1
    result += abs( c_q - down ) -1
    result += abs( leftUp - r_q ) -1
    result+= abs(rightUp - r_q ) -1
    result += abs( r_q - leftDown ) -1
    result += abs( r_q - rightDown ) -1




    print(result)
