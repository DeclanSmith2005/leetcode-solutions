# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessHead = ListNode()
        lessPtr = lessHead
        greatHead= ListNode()
        greatPtr = greatHead
        ptr  = head
        while ptr != None:
            if ptr.val < x:
                lessPtr.next = ptr
                lessPtr = lessPtr.next
            else:
                greatPtr.next= ptr
                greatPtr = greatPtr.next
            ptr = ptr.next
        greatPtr.next = None
        lessPtr.next = greatHead.next
        return lessHead.next
        