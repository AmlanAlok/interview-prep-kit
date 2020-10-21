from datetime import datetime




class Solution:

    def main(self):

        input = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
        self.get_max_output(input)

    def get_max_output(self, prices):

        l = len(prices)

        if l == 1:
            return 0

        diff = [0]

        for i, v in enumerate(prices):
            if i > 0:
                diff.append(v - prices[i - 1])

        print('diff = ', diff)

        p = []
        temp = []
        sum = 0

        for n in diff:

            if n >= 0:
                sum += n

            elif n < 0:
                if sum > 0:
                    p.append(sum)
                    sum = 0
                else:
                    temp.append(n)
                    sum = sum + n
                # p.append(n)

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