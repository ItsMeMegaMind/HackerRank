#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] > grid[i + 1][j] and grid[i][j] > grid[i][j + 1] and grid[i][j] > grid[i - 1][j] and grid[i][
                j] > grid[i][j - 1]:
                grid[i] = grid[i][:j] + "X" + grid[i][j + 1:]
    for i in grid:
        print(i)


if __name__ == '__main__':

    n = int(input().strip())
    grid = []
    temp = 0
    for _ in range(n):
        temp = str(input().strip())
        grid.append(temp)
    cavityMap(grid)
