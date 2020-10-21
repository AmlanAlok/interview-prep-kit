from datetime import datetime

'''
This is my solution which was my first attempt
'''

def find_median(a):
    l = len(a)
    print('l of a =', l)
    p = int(l / 2)
    print('p =', p)

    if l % 2 == 0:
        print('even')
        print((a[p] + a[p - 1]) / 2.0)
        return (a[p] + a[p - 1]) / 2.0
    else:
        print('odd')
        print(a[p])
        return a[p]


def merge_and_sort(a, b):

    c1 = a + b
    c1.sort()
    return c1


a, b = [], []

# for i in range(1, 51):
#     a.append(i)
#
# for i in range(51, 101):
#     b.append(i)

for i in range(1, 1001, 2):
    a.append(i)

for i in range(2, 1002, 2):
    b.append(i)

print('a =', a)
print('b =', b)

d1 = datetime.now()

c = merge_and_sort(a, b)

print('c =', c)

median = find_median(c)

print('median = ', median)

print('Time Taken = ', datetime.now() - d1)

# median =  500.5
# Time Taken =  0:00:00.000246


# [101,102,103,104,105,106,107,108,109,110,111,112]
# [113,114,115,116,117,118,119,120,121]

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
# [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]