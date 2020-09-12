#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    a = sorted(ar)
    # print('a =', a)
    pair = 0

    i=0
    while i < len(a)-1:
        # print(i, a[i], a[i+1])
        if a[i] == a[i+1]:
            pair = pair + 1
            i = i+2
        else:
            i=i+1

    return pair


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
