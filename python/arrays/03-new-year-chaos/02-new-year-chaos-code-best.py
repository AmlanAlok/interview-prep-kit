#!/bin/python3

# ------------------------------
# Best Solution
# ------------------------------

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the minimumBribes function below.
def minimumBribes(q):

    m=0
    first = 1
    second = 2
    third = 3

    for i in range(len(q)):
        if q[i] == first:
            first = second
            second = third
            third+=1
        elif q[i] == second:
            m+=1
            second = third
            third+=1
        elif q[i] == third:
            m+=2
            third+=1
        else:
            return 'Too chaotic'

    return m



if __name__ == '__main__':

    with open('input10.txt') as f:
        t = int(f.readline())
        # print(t)

        for t_itr in range(t):

            n = int(f.readline())
            q = list(map(int, f.readline().rstrip().split()))

            d1 = datetime.now()
            output = minimumBribes(q)
            print(output)

            print(datetime.now()-d1)



    # t = int(input())
    #
    # for t_itr in range(t):
    #     n = int(input())
    #
    #     q = list(map(int, input().rstrip().split()))
    #
    #     d1 = datetime.now()
    #     output = minimumBribes(q)
    #     print(output)
    #
    #     # print(datetime.now()-d1)




# 1201
# 0:00:00.000190
# 1208
# 0:00:00.000175
# Too chaotic
# 0:00:00.000007
# 1196
# 0:00:00.000172
# Too chaotic
# 0:00:00.000007
# 1196
# 0:00:00.000170
# Too chaotic
# 0:00:00.000006
# Too chaotic
# 0:00:00.000005
# Too chaotic
# 0:00:00.000006
# 1210
# 0:00:00.000184
