import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    magicSquares = [
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8]
    ]
    diff = []
    for l in magicSquares:
        diff.append(sum([abs(s[i] - l[i]) for i in range(9)]))
    return min(diff)

if __name__ == '__main__':
    s = []
    for _ in range(3):
        temp = [int(i) for i in input().split()]
        s+=temp
    result = formingMagicSquare(s)
    print(result)