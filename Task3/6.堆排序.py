"""
堆排序的基本思想是：将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。
将其与末尾元素进行交换，此时末尾就为最大值。
然后将剩余n-1个元素重新构造成一个堆，这样会得到n个元素的次小值。
如此反复执行，便能得到一个有序序列了
"""
heap_size = 0
Left = lambda i: 2 * i + 1
Right = lambda i: 2 * i + 2


def max_heap(arr, i):
    while True:
        l, r = Left(i), Right(i)
        # 小顶堆
        smallest = l if l < heap_size and arr[i] > arr[l] else i
        smallest = r if r < heap_size and arr[smallest] > arr[r] else smallest
        if i == smallest:
            break
        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest


def build_max_heap(arr):
    global heap_size
    heap_size = len(arr)
    # 从第一个非叶子节点开始
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heap(arr, i)


def heap_sort(arr):
    global heap_size
    build_max_heap(arr)
    for i in range(len(arr) - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap_size -= 1
        max_heap(arr, 0)
    return arr


array = [0, 1, 2, 3, 4, 3, 2, 1, 0, 5, 6, 7, 8, 9]
sorted_array = heap_sort(array)
print(sorted_array)
