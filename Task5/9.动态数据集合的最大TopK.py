Left = lambda x: 2 * x + 1
Right = lambda x: 2 * x + 2


class MaxHeap:
    def __init__(self, K):
        self.heap = []
        self.heap_size = K

    def min_heap(self, i):
        while True:
            left = Left(i)
            right = Right(i)

            if right < self.heap_size and self.heap[right] < self.heap[i]:
                min_size = right
            else:
                min_size = i

            if left < self.heap_size and self.heap[left] < self.heap[min_size]:
                min_size = left
            else:
                pass

            if i == min_size:
                break
            self.heap[i], self.heap[min_size] = self.heap[min_size], self.heap[i]

    def build(self):
        for i in range(self.heap_size // 2 - 1, -1, -1):
            self.min_heap(i)

    def put(self, value):
        if len(self.heap) < self.heap_size:
            self.heap.append(value)
        else:
            if value > self.heap[0]:
                self.heap[0] = value
                self.build()


topK = MaxHeap(3)
topK.put(1)
print(topK.heap)
topK.put(2)
print(topK.heap)
topK.put(3)
print(topK.heap)
topK.put(4)
print(topK.heap)
topK.put(4)
print(topK.heap)
topK.put(5)
print(topK.heap)
topK.put(5)
print(topK.heap)
