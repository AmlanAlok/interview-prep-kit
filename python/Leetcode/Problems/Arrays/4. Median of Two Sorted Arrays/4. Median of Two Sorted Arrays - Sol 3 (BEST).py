from datetime import datetime


def kth(a, b, k):
    print('a, b, k = ', a, b, k)
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2, len(b) // 2
    ma, mb = a[ia], b[ib]

    # when k is bigger than the sum of a and b's median indices
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return kth(a, b[ib + 1:], k - ib - 1)
        else:
            return kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return kth(a[:ia], b, k)
        else:
            return kth(a, b[:ib], k)


def find_median(A, B):
    l = len(A) + len(B)
    print('total l = ', l)
    if l % 2 == 1:
        print('odd')
        return kth(A, B, l // 2)
    else:
        print('even')
        return (kth(A, B, l // 2) + kth(A, B, l // 2 - 1)) / 2.


a, b = [], []

for i in range(1, 1001, 2):
    a.append(i)

for i in range(2, 1002, 2):
    b.append(i)

print('a =', a)
print('b =', b)

d1 = datetime.now()

median = find_median(a, b)

print('median = ', median)

print('Time Taken = ', datetime.now() - d1)



# median =  500.5
# Time Taken =  0:00:00.001485