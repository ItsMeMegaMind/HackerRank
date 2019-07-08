#!/bin/python3

import math
import os
import random
import re
import sys


def timeInWords(h, m):
    out=''
    if(m==00):
        out+=number(h)
        out+=" o' clock"
    elif(m==1):
        out += number(m)
        out += " minute past "
        out += number(h)
    elif (m<30 and m!=15):
        out+= number(m)
        out+= " minutes past "
        out+= number(h)
    elif (m==15):
        out += "quarter past "
        out += number(h)
    elif(m==30):
        out += "half past "
        out += number(h)
    elif (m==59):
        out+= number(60 - m)
        out+= " minute to "
        out+= number(h+1)
    elif (m>30 and m!=45):
        out+= number(60 - m)
        out+= " minutes to "
        out+= number(h+1)
    elif (m==45):
        out += "quarter to "
        out += number(h+1)
    return out


def number(Number):
    if 1 <= Number < 19:
        return num2words1[Number]
    elif 20 <= Number <= 99:
        tens, below_ten = divmod(Number, 10)
        return num2words2[tens - 2] + ' ' + num2words1[below_ten]
    else:
        print("Number out of range")


if __name__ == '__main__':
    num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                  6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
                  11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                  15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    h = int(input())
    m = int(input())
    result = timeInWords(h, m)
    print(result.lower())




