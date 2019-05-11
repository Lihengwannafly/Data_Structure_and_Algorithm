import ctypes


class DynamicArray(object):
    def __init__(self):
        self._size = 0
        self._capacity = 10
        self._array = self._make_array(self._capacity)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if 0 <= index < self._size:
            return self._array[index]
        else:
            raise IndexError('Out of range')

    """
    末尾插入
    """

    def append(self, obj):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._size] = obj
        self._size += 1

    @staticmethod
    def _make_array(capacity):
        return (capacity * ctypes.py_object)()
        # return [None] * capacity

    def _resize(self, capacity):
        tmp = self._make_array(capacity)
        for k in range(self._size):
            tmp[k] = self._array[k]

        self._array = tmp
        self._capacity = capacity

    """
    增加
    """

    def insert(self, index, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = value
        self._size += 1

    """
    删除
    """
    def remove(self, value):
        for i in range(self._size):
            if self._array[i] == value:
                for j in range(i, self._size - 1):
                    self._array[j] = self._array[j + 1]
                self._array[self._size - 1] = None
                self._size -= 1
                return

        raise ValueError("value not found")

    """
    改
    """
    def change(self, index, value):
        if 0 <= index < self._size:
            self._array[index] = value

        else:
            raise IndexError('Out of range')

    def _print(self):
        for i in range(self._size):
            print(self._array[i], end=' ')
        print()

