"""
基本思想
先将序列分成较多个子序列分别进行排序，再分成较少个子序列分别进行排序，直到最后为一个序列排序
希尔排序采用每隔固定距离选取一个数的方法划分子序。其中间隔距离称为增量
"""


def shell_sort(arr):
    n = len(arr)
    gap = n >> 1
    while gap > 0:
        for i in range(gap, n):
            j = i
            while (j - gap) >= 0:
                if arr[j] > arr[j - gap]:
                    arr[j], arr[j - gap] = arr[j - gap], arr[j]
                    j -= gap
                else:
                    break
        gap >>= 1

    return arr


array = [0, 1, 2, 3, 4, 3, 2, 1, 0, 5, 6, 7, 8, 9]
sorted_array = shell_sort(array)
print(sorted_array)
