#!/bin/python3

import math
import os
import random
import re
import sys


# next (c = array, x = current position, l = length of array c , p = jumps)
def next(c, x, l, p):
    print(c, x, l, p)

    if x == l - 1:
        return p
    elif x < l - 1:
        if x + 2 <= l - 1 and c[x + 2] == 0:
            x += 2
            p += 1
            return next(c, x, l, p)
        elif c[x + 1] == 0:
            x += 1
            p += 1
            return next(c, x, l, p)
        else:
            return -1
    else:
        return -1


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    return next(c, 0, len(c), 0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
