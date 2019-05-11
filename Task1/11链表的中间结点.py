"""
快慢两个指针，快指针走到尾部时，慢指针刚好走到中间
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            if fast.next.next:
                fast = fast.next.next
            else:
                break
        return slow
