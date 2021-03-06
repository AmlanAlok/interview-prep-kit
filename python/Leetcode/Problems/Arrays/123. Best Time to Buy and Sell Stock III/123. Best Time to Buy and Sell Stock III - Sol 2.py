from datetime import datetime


class Solution:

    def main(self):

        a = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
        print('a =', a)
        d1 = datetime.now()

        output = self.get_max_output(a)

        print('output =', output)

        print('Time taken = ', datetime.now() - d1)

    def get_max_output(self, prices):

        l = len(prices)

        if l == 1:
            return 0

        # ----------------------------------------
        diff = [0]

        for i, v in enumerate(prices):
            if i > 0:
                diff.append(v - prices[i - 1])

        print('diff = ', diff)
        # ----------------------------------------

        p = []
        temp = []
        sum = 0
        n_check = False

        for i, v in enumerate(diff):
            print('sum =', sum, 'v =', v)

            if v > 0:
                sum += v

            elif v < 0:

                if sum > 0:
                    if n_check:
                        prev = p[-1]
                        if len(temp) > 0:
                            new = max(p[-1] + sum, p[-1] + sum - temp[-1])
                        else:
                            new = p[-1] + sum
                        p[-1] = new
                        print('p1 =', p)
                        n_check = False
                    else:
                        p.append(sum)
                        print('p2 =', p)
                        n_check = True
                    sum = 0
                    sum += v

                    temp.append(v)

                else:
                    print('3rd')
                    if n_check:
                        sum = 0
                        n_check = False
                    else:
                        print('This scenario must not happen')

        if sum >= 0:
            p.append(sum)

        print('p =', p)

        p.sort()

        plen = len(p)

        if plen == 0:
            return 0
        elif plen == 1:
            return p[0]
        else:
            return p[-1] + p[-2]





solution = Solution()
solution.main()