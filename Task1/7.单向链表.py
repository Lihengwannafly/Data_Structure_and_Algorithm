class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkList(object):
    def __init__(self):
        """初始化链表"""
        self.head = None
        self.len = 0

    def append(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            pre = self.head
            while pre.next:
                pre = pre.next
            pre.next = node
        self.len += 1

    def insert(self, index, val):

        if index > self.len:
            raise IndexError('Out of range')
        else:
            node = Node(val)
            if index == 0:
                node.next = self.head
                self.head = node
            elif index == self.len:
                self.append(val)
            else:
                head = self.head
                cur_index = 0
                while head:
                    if cur_index + 1 == index:
                        nex = head.next
                        head.next = node
                        node.next = nex
                        break
                    cur_index += 1
                    head = head.next
        self.len += 1

    def delete(self, index):
        if index >= self.len:
            raise IndexError('Out of range')
        else:
            if index == 0:
                self.head = self.head.next
            else:
                head = self.head
                cur_index = 0
                while head:
                    if cur_index + 1 == index:
                        head.next = head.next.next
                        break
                    cur_index += 1
                    head = head.next
        self.len += 1

    def reversed(self):
        pre = None
        cur = self.head
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        self.head = pre


linkList = LinkList()
linkList.append(6)
linkList.append(7)
linkList.insert(0, 1)
linkList.reversed()
head = linkList.head
while head:
    print(head.val)
    head = head.next
