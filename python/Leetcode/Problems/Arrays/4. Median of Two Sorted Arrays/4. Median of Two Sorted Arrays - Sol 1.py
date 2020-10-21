from datetime import datetime


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

    i1, j1, k1, c1 = 0, 0, 0, []

    print(a, b)
    print(len(a), len(b))

    while i1 < len(a) and j1 < len(b):
        # print('i =', i1)
        if a[i1] < b[j1]:
            # print('1')
            c1.append(a[i1])
            i1 += 1
        else:
            # print('2')
            c1.append(b[j1])
            j1 += 1
        # k1 += 1

        # print('i1, j1, k1 =', i1, j1, k1)

    while i1<len(a):
        c1.append(a[i1])
        i1 += 1

    while j1<len(b):
        c1.append(b[j1])
        j1 += 1

    # print('output c1 =', c1)

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

# r = b + a

c = merge_and_sort(a, b)

print('c =', c)

median = find_median(c)

print('median = ', median)

print('Time Taken = ', datetime.now() - d1)

# median =  50.5
# Time Taken =  0:00:00.000091
