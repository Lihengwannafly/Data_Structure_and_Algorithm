class MergeSortedK(object):
    def __init__(self, heap):
        self.heap = heap
        self.sorted = []
        self.heap_size = len(self.heap)

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def min_heap(self, i):

        while True:
            left = self.left(i)
            right = self.right(i)
            if right < self.heap_size and self.heap[right][0] < self.heap[i][0]:
                min_index = right
            else:
                min_index = i

            if left < self.heap_size and self.heap[left][0] < self.heap[min_index][0]:
                min_index = left

            else:
                pass

            if min_index == i:
                break

            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]

    def build_heap(self):
        for i in range(self.heap_size // 2 - 1, -1, -1):
            self.min_heap(i)

    def merge(self):
        while self.heap:
            self.build_heap()
            tmp = self.heap[0].pop(0)
            if not self.heap[0]:
                self.heap.pop(0)
                self.heap_size -= 1
            self.sorted.append(tmp)


sorted_K = [[1, 2, 3, 4, 5, 6], [1, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
merge_sorted = MergeSortedK(sorted_K)
merge_sorted.merge()
print(merge_sorted.sorted)
