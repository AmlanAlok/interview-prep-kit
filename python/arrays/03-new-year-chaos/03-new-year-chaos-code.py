from datetime import datetime

def count_inversion(lst):
    return merge_count_inversion(lst)[1]

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count

if __name__ == '__main__':

    with open('input10.txt') as f:
        t = int(f.readline())

        for t_itr in range(t):

                d1 = datetime.now()
                N=int(f.readline())
                a=list(map(int,f.readline().split()))
                if any(a[i]-(i+1)>2 for i in range(N)):
                    print("Too chaotic")
                else:
                    print(count_inversion(a))

                print(datetime.now() - d1)




# 1201
# 0:00:00.003192
# 1208
# 0:00:00.003172
# Too chaotic
# 0:00:00.000214
# 1196
# 0:00:00.003133
# Too chaotic
# 0:00:00.000196
# 1196
# 0:00:00.003068
# Too chaotic
# 0:00:00.000192
# Too chaotic
# 0:00:00.000177
# Too chaotic
# 0:00:00.000188
# 1210
# 0:00:00.003054