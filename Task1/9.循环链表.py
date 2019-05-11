"""
插入或者删除的时候，如果操作的节点在tail或者head，需要注意，tail.next->head.next，其余和单向链表基本相同
"""
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkList(object):
    def __init__(self):
        """初始化链表"""
        self.head = None
        self.tail = None
        self.len = 0

    def append(self, val):
        """
        1.head 为none :head-->node
        2.tail.nex-->node
        :param data:
        :return:
        """
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        self.len += 1

    def insert(self, index, val):
        """
        1.index 插入节点位置包括正负数
        2.找到index-1-->pre_node的节点
        3.pre_node.next-->node
          node.next-->pre_node.next.next
        4.head
        :param index:
        :param data:
        :return:
        """
        if index > self.len:
            raise IndexError('Out of range')
        else:
            node = Node(val)
            if index == 0:
                node.next = self.head
                self.head = node
                self.tail.next = self.head
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
                self.tail.next = self.head
            else:
                head = self.head
                cur_index = 0
                while head:
                    if cur_index + 1 == index:
                        if index == self.len:
                            self.tail = head
                            self.tail.next = self.head
                        else:
                            head.next = head.next.next
                        break
                    cur_index += 1
                    head = head.next
        self.len += 1


linkList = LinkList()
linkList.append(6)
linkList.append(7)
linkList.insert(0, 1)
head = linkList.head
while head:
    print(head.val)
    head = head.next
