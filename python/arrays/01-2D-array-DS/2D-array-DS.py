#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    print(arr)
    print(len(arr))
    print(len(arr[0]))

    p = []

    for i in range(len(arr[0]) - 2):
        for j in range(len(arr) - 2):
            # print(i, j)
            sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
                  arr[i + 2][j + 2]
            p.append(sum)

    # print('p len = ', len(p))

    # z = sorted(p)
    # print('z= ', z)

    # return z[-1]
    return max(p)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
