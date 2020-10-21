from datetime import datetime
import sys

'''
Source = https://www.youtube.com/watch?v=LPFhl65R7ww

This is the best solution I found with explanation in a youtube video.
And, this is a beautiful piece of code. You must understand and remember this by heart.
Solution complexity is O( log( min(m, n))) where m and n are the size of the two input arrays.
'''


class Solution:

    def main(self):

        a, b = [], []

        # b = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]
        # a = [113, 114, 115, 116, 117, 118, 119, 120, 121]

        # a = [1, 2]
        # b = [3, 4]

        for i in range(1, 1001, 2):
            a.append(i)

        for i in range(2, 1002, 2):
            b.append(i)

        print('a =', a)
        print('b =', b)

        d1 = datetime.now()

        median = self.find_median(a, b)

        print('median = ', median)

        print('Time Taken = ', datetime.now() - d1)

    def find_median(self, array_x, array_y):

        x = len(array_x)
        y = len(array_y)

        min_int_value = sys.maxsize * -1
        max_int_value = sys.maxsize

        if x > y:
            return self.find_median(array_y, array_x)

        print('length x =', x, ', length y =', y)

        total_len = x + y
        print('total length = ', total_len)

        low = 0
        high = x

        while low <= high:
            print('low = {}, high = {}'.format(low, high))
            x_partition = (low + high) // 2
            print('x_partition = ', x_partition)

            y_partition = (total_len + 1) // 2 - x_partition
            print('y_partition = ', y_partition)

            x_left_max = min_int_value if x_partition == 0 else array_x[x_partition - 1]
            x_right_min = max_int_value if x_partition == x else array_x[x_partition]

            y_left_max = min_int_value if y_partition == 0 else array_y[y_partition - 1]
            y_right_min = max_int_value if y_partition == y else array_y[y_partition]

            if x_left_max <= y_right_min and y_left_max <= x_right_min:

                print('x_left_max = ', x_left_max)
                print('y_right_min = ', y_right_min)
                print('y_left_max = ', y_left_max)
                print('x_right_min = ', x_right_min)

                if total_len % 2 == 0:
                    return (max(x_left_max, y_left_max) + min(x_right_min, y_right_min)) / 2
                else:
                    return max(x_left_max, y_left_max)

            elif x_left_max > y_right_min:
                high = x_partition - 1

            else:
                low = x_partition + 1


solution = Solution()
solution.main()
