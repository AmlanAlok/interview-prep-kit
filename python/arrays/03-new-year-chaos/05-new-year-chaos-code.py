
from datetime import datetime

if __name__ == '__main__':

    with open('input10.txt') as f:

        T = int(f.readline())
        for a0 in range(T):

            d1 = datetime.now()
            n = int(f.readline().strip())
            q = [int(q_temp) for q_temp in f.readline().strip().split(' ')]
            swaps = [0]*len(q)
            while True:
                round_swaps = 0
                for i in range(1, len(q)):
                    if q[i - 1] > q[i]:
                        swaps[q[i - 1]-1] += 1
                        round_swaps += 1
                        q[i - 1], q[i] = q[i], q[i - 1]
                if not round_swaps:
                    break
            if any(s > 2 for s in swaps):
                print("Too chaotic")
            else:
                print(sum(swaps))

            print(datetime.now() - d1)