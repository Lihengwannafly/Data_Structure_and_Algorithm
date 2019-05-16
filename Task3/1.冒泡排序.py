"""
它重复地走访过要排序的元素列，依次比较两个相邻的元素，如果他们的顺序（如从大到小、首字母从A到Z）错误就把他们交换过来。
走访元素的工作是重复地进行直到没有相邻元素需要交换，也就是说该元素列已经排序完成。
"""


def bubble_sort(arr):
    n = len(arr)
    # 一共进行几轮列表比较,一共是(n - 1)轮
    for i in range(n - 1):
        # 每一轮的比较,注意range的变化,这里需要进行n - 1 - i的比较,注意-i的意义(可以减少比较已经排好序的元素)
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


array = [0, 1, 2, 3, 4, 3, 2, 1, 0, 5, 6, 7, 8, 9]
sorted_array = bubble_sort(array)
print(sorted_array)
