#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime


# Complete the minimumSwaps function below.
def minimumSwaps(a):

    index_dict = {v: i for i, v in enumerate(a)}

    # print(index_dict)

    i = 0
    swap_count = 0
    while i < len(a):

        if a[i] != i + 1:
            # expectedNumIndex = a.index(i + 1)
            expectedNumIndex = index_dict[i+1]
            a[i], a[expectedNumIndex] = a[expectedNumIndex], a[i]

            index_dict[a[expectedNumIndex]] = expectedNumIndex
            index_dict[a[i]] = i
            swap_count += 1

        i += 1
    return swap_count


if __name__ == '__main__':
    # 99984

    with open('input10.txt') as f:

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

        d1 = datetime.now()
        n = int(f.readline())

        arr = list(map(int, f.readline().rstrip().split()))

        res = minimumSwaps(arr)

        print(res)
        print(datetime.now()-d1)

        # fptr.write(str(res) + '\n')
        #
        # fptr.close()
