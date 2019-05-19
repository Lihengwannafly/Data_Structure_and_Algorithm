class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def move_to_tail(self, cur):
        cur.pre = self.tail.pre
        cur.pre.next = cur
        self.tail.pre = cur
        cur.next = self.tail

    def get(self, key: int) -> int:
        if not self.hash.get(key):
            return -1
        cur = self.hash.get(key)
        cur.pre.next = cur.next
        cur.next.pre = cur.pre
        self.move_to_tail(cur)
        return cur.value

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.hash.get(key).value = value
            return
        if len(self.hash) == self.capacity:
            self.hash.pop(self.head.next.key)
            self.head.next = self.head.next.next
            self.head.next.pre = self.head
        insert = Node(key, value)
        self.hash[key] = insert
        self.move_to_tail(insert)


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
