def quick_sort(arr, start, end):
    if start >= end:
        return arr

    base = arr[start]
    left = start
    right = end

    while start < end:
        while start < end and arr[end] <= base:
            end -= 1

        arr[start] = arr[end]

        while start < end and arr[start] >= base:
            start += 1

        arr[end] = arr[start]

    arr[start] = base

    quick_sort(arr, left, start-1)
    quick_sort(arr, start+1, right)

    return arr


array = [0, 1, 2, 3, 4, 3, 2, 1, 0, 5, 6, 7, 8, 9]
sorted_array = quick_sort(array, 0, len(array) - 1)
print(sorted_array)