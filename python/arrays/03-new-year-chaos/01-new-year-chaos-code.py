#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the minimumBribes function below.
def minimumBribes(q):

    # a = sorted(q)

    m = 0
    w = 0
    e = 0

    for i in range(len(q)):
        if q[i]-i>3:
            return 'Too chaotic'
        elif q[i]!=i+1:
            for j in range(i+1,len(q)):
                # print(i, j)
                if q[i]>q[j]:
                    m+=1
                else:
                    w+=1
        elif q[i]==i+1:
            e+=1
            for j in range(i+1, len(q)):

                if q[i]>q[j]:
                    # print(q[i], q[j])
                    m+=1
                else:
                    w+=1

        # for j in range(i+1,len(q)):
        #         # print(i, j)
        #         if q[i]>q[j]:
        #             m+=1
        #         else:
        #             w+=1

    # print('w =', w)
    # print('e =', e)
    # print('len(q) = ', len(q))
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
# 0:00:00.050136
# 1208
# 0:00:00.044587
# Too chaotic
# 0:00:00.000007
# 1196
# 0:00:00.044329
# Too chaotic
# 0:00:00.000007
# 1196
# 0:00:00.045006
# Too chaotic
# 0:00:00.000006
# Too chaotic
# 0:00:00.000028
# Too chaotic
# 0:00:00.000005
# 1210
# 0:00:00.044916