#!/bin/python3

import math
import os
import random
import re
import sys


def get_occur(s):
    p = 0
    for x in s:
        if x == 'a':
            p += 1
        else:
            continue

    return p


# Complete the repeatedString function below.
def repeatedString(s, n):
    p = get_occur(s)

    m = int(n / len(s))
    r = n % len(s)
    print(r, p, m)

    z = s[0:r]
    print('z=', z)

    q = get_occur(z)
    print('q=', q)

    return p * m + q


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
