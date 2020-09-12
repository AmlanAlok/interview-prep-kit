#!/bin/python3

from datetime import datetime

if __name__ == '__main__':

    with open('input10.txt') as f:
        t = int(f.readline())

        for t_itr in range(t):

            d1 = datetime.now()
            f.readline()
            q = [int(x) for x in f.readline().split()]
            bribes = 0
            valid = True
            for i in reversed(range(len(q))):
                v = i + 1
                if q[-1] == v:
                    q.pop(-1)
                elif len(q) > 1 and q[-2] == v:
                    q.pop(-2)
                    bribes += 1
                elif len(q) > 2 and q[-3] == v:
                    q.pop(-3)
                    bribes += 2
                else:
                    valid = False
                    break
            if valid:
                print(bribes)
            else:
                print("Too chaotic")

            print(datetime.now() - d1)





# 1201
# 0:00:00.000846
# 1208
# 0:00:00.000768
# Too chaotic
# 0:00:00.000240
# 1196
# 0:00:00.000778
# Too chaotic
# 0:00:00.000238
# 1196
# 0:00:00.000755
# Too chaotic
# 0:00:00.000237
# Too chaotic
# 0:00:00.000225
# Too chaotic
# 0:00:00.000314
# 1210
# 0:00:00.001242