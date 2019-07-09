#!/bin/python
nk = input().split()
n = int(nk[0])
k = int(nk[1])
r_qC_q = input().split()

r_q = int(r_qC_q[0])

c_q = int(r_qC_q[1])

up = n - r_q
down = r_q - 1
right = n - c_q
left = c_q - 1

up_left = min(n - r_q, c_q - 1)
up_right = n - max(c_q, r_q)
bLeft = min(r_q, c_q) - 1
bRight = min(r_q - 1, n - c_q)

for _ in range(k):
    obsRow, obsCol = map(int, input().split(' '))

    if obsRow == r_q:
        if obsCol > c_q:
            up = min(up, obsCol - c_q - 1)
        else:
            down = min(down, c_q - obsCol - 1)

    elif obsCol == c_q:
        if obsRow > r_q:
            right = min(right, obsRow - r_q - 1)
        else:
            left = min(left, r_q - obsRow - 1)

    elif abs(obsCol - c_q) == abs(obsRow - r_q):

        if obsCol > c_q and obsRow > r_q:
            up_right = min(up_right, obsCol - c_q - 1)

        elif obsCol > c_q and obsRow < r_q:
            bRight = min(bRight, obsCol - c_q - 1)

        elif obsCol < c_q and obsRow > r_q:
            up_left = min(up_left, c_q - obsCol - 1)

        elif obsCol < c_q and obsRow < r_q:
            bLeft = min(bLeft, c_q - obsCol - 1)

print(up + down + right + left + up_left + up_right + bLeft + bRight)