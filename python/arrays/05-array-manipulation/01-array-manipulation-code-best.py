#!/bin/python3

import math
import os
import random
import re
import sys
from _datetime import datetime


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    dic = {i: 0 for i, v in enumerate(range(n), 1)}
    # print(dic)
    # print(dic[2])

    for b in queries:
        for x in range(b[0], b[1] + 1):
            dic[x] += b[2]

    final = list(dic.values())
    # print('final =', final)
    return max(final)


def arrayManipulationTwo(n, queries):
    # arr = [0 for i in enumerate(range(n + 2))]
    arr = [0] * (n + 2)                    # this way of creating a list with default value is much more efficient
    # print(a)

    for z in queries:
        a, b, k = z[0], z[1], z[2]
        arr[a] += k
        arr[b + 1] -= k

    # print(a)

    # for c in range(1, len(a)):
    #     a[c] = a[c] + a[c - 1]

    max = sys.maxsize * -1
    summ = 0

    # print(arr)
    # for c in range(len(arr)):
    for x in arr:               # this for loop instead of the upper one brought the time down to 0.75 sec from 1 sec
        summ += x
        # print(summ)
        if summ > max:
            max = summ

    # print('-----')

    return max
    # return max(a)


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

        result = arrayManipulationTwo(n, queries)

        print(result)
        print(datetime.now() - d1)
