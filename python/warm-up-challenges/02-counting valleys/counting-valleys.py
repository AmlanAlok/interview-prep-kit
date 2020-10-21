#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here

    e = 0
    v = 0

    for x in path:
        if x == 'U':

            e = e + 1
            if e == 0:
                v = v + 0.5

        elif x == 'D':

            if e == 0:
                v = v + 0.5
            e = e - 1

    return int(v)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
