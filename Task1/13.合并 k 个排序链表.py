"""
分治法，将lists最终拆分为两两合并，然后就简化为之前做过的两个有序链表合并
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self.mergeLists(lists)

    def mergeLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            l1 = lists[0]
            l2 = lists[1]
            l = self.mergeTwoLists(l1, l2)
            return l
        middle = len(lists) // 2
        l1 = self.mergeLists(lists[:middle])
        l2 = self.mergeLists(lists[middle:])
        l = self.mergeTwoLists(l1, l2)
        return l

    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        tmp = head
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next

        if l1:
            tmp.next = l1

        if l2:
            tmp.next = l2

        return head.next
