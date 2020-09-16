#!/bin/python3


''' SOURCE = https://allhackerranksolutions.blogspot.com/2019/01/array-manipulation-hacker-rank-solution.html '''

import math
import os
import random
import re
import sys
from datetime import datetime


def arrayManipulation(n, queries):
    summ, maxx = 0, 0
    arr = [0] * (n + 1)
    for i in queries:
        a, b, k = i[0], i[1], i[2]
        arr[a - 1] += k
        arr[b] -= k
    # arr = arr[:n]
    for i in arr:
        summ += i
        # maxx = max(summ, maxx)
        if summ > maxx:                     # I added this if block as it halfed the time taken
            maxx = summ
    return maxx


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # 2497169732 for input07
    # 2484930878 for input08
    # 2490686975 for input13
    with open('input08.txt') as f:

        d1 = datetime.now()
        nm = f.readline().split()

        n = int(nm[0])

        m = int(nm[1])

        queries = []

        for _ in range(m):
            queries.append(list(map(int, f.readline().rstrip().split())))

        result = arrayManipulation(n, queries)

        print(result)
        print(datetime.now() - d1)
