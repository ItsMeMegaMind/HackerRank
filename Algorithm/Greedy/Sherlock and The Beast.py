#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the decentNumber function below.





if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        out = ""
        fives = 0
        threes = 0
        while (n > 0):
            if (n % 3 == 0):
                while (n > 0):
                    fives += 1
                    n -= 3
            elif (n % 5 == 0):
                threes += 1
                n -= 5
            else:
                fives += 1
                n -= 3;
            if (n < 0):
                out = -1
            else:
                out = '5' * (fives * 3)
                out += '3' * (threes * 5)
        print(out)
