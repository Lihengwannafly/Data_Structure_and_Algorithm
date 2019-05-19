class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class ChainHashMap(object):
    def __init__(self):
        self.chain_hash = dict()

    def insert(self, key, val):
        node = ListNode(val)
        if key not in self.chain_hash:
            self.chain_hash[key] = node
        else:
            head = self.chain_hash[key]
            while head.next:
                head = head.next
            head.next = node

    def search(self, key, val):
        if key not in self.chain_hash:
            raise KeyError()
        head = self.chain_hash[key]
        while head.next:
            if head.val == val:
                return head
            else:
                print("Value not in hash map")

    def delete(self, key, val):
        if key not in self.chain_hash:
            raise KeyError()
        head = self.chain_hash[key]
        if head.val == val:
            if not head.next:
                del self.chain_hash[key]
            else:
                self.chain_hash[key] = head.next
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                print("Value not in hash map")
                break

    def print_chain_hash(self):
        for key in self.chain_hash.keys():
            head = self.chain_hash[key]
            while head:
                print(key, head.val)
                head = head.next


ch = ChainHashMap()
ch.insert(5, 10)
ch.insert(5, 11)
ch.print_chain_hash()
ch.insert(1, 2)
ch.insert(1, 3)
ch.print_chain_hash()
ch.delete(1, 6)
ch.print_chain_hash()
