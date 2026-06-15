# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # get length
        n = 0
        ptr = head
        while ptr:
            n += 1
            ptr = ptr.next
        ptr, prev = head, None
        for i in range(n//2):
            prev = ptr
            ptr = ptr.next
        if ptr and prev:
            prev.next = ptr.next
        return head if prev else None
