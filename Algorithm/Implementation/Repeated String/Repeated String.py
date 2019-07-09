#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()

    n = int(input())

    a,b = divmod(n,len(s))
    print(a*s.count('a') + s[:b].count('a'))