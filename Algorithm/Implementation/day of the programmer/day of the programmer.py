#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year > 1918:
        print(13 - isLeapYearG(year), '09', year, sep='.')
    elif year == 1918:
        print(26, '09', year, sep='.')
    else:
        print(13 - isLeapYearJ(year), '09', year, sep='.')


def isLeapYearJ(year):
    return 1 if year % 4 == 0 else 0


def isLeapYearG(year):
    if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
        return 1
    else:
        return 0


if __name__ == '__main__':
    year = int(input().strip())

    dayOfProgrammer(year)

