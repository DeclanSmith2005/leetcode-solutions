# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev, lp, rp = None, l1, l2
        carry = 0
        while lp and rp:
            total = lp.val + rp.val + carry
            lp.val = total % 10
            carry = total > 9
            prev = lp
            lp, rp = lp.next, rp.next
        if rp:
            prev.next = rp
        lp = prev.next
        while lp and carry:
            total = lp.val + carry
            lp.val = total %10
            carry = total > 9
            prev = lp
            lp = lp.next
        if carry:
            prev.next = ListNode(1)
        return l1

