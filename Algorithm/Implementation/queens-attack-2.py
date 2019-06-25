#!/bin/python3


import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):

    out = right(n,r_q,c_q,obstacles)
    out += left(n, r_q, c_q, obstacles)
    out += up(n, r_q, c_q, obstacles)
    out += down(n, r_q, c_q, obstacles)
    out += upL(n, r_q, c_q, obstacles)
    out += upR(n, r_q, c_q, obstacles)
    out += downL(n, r_q, c_q, obstacles)
    out += downR(n, r_q, c_q, obstacles)
    return out



def right(n,y,x,obstacles):
    out = 0
    while (x<=n and ([y,x] not in obstacles)  ):
        out+=1
        x+=1
    return (out - 1)

def left(n,y,x,obstacles):
    out = 0
    while (x>=1 and ([y,x] not in obstacles)  ):
        out+=1
        x-=1
    return (out - 1)

def down(n,y,x,obstacles):
    out = 0
    while (y>=1 and ([y,x] not in obstacles)  ):
        out+=1
        y-=1
    return (out - 1)

def up(n,y,x,obstacles):
    out = 0
    while (y<=n and ([y,x] not in obstacles)  ):
        out+=1
        y+=1
    return (out - 1)

def upR(n,y,x,obstacles):
    out = 0
    while (y<=n  and x<=n  and ([y,x] not in obstacles)  ):
        out+=1
        y+=1
        x+=1
    return (out - 1)

def upL(n,y,x,obstacles):
    out = 0
    while (y<=n  and x>0 and ([y,x] not in obstacles)  ):
        out+=1
        y+=1
        x-=1
    return (out - 1)

def downL(n,y,x,obstacles):
    out = 0
    while (y>0  and x>0 and ([y,x] not in obstacles)  ):
        out+=1
        y-=1
        x-=1
    return (out - 1)

def downR(n,y,x,obstacles):
    out = 0
    while (y>0  and x<=n and ([y,x] not in obstacles)  ):
        out+=1
        y-=1
        x+=1
    return (out - 1)

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
        print(_)
    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)
