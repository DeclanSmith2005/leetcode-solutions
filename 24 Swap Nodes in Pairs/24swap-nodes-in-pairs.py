# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        og = first = head.next
        second = head
        prev = None
        while first:
            temp = first.next
            first.next = second
            second.next = temp
            if prev:
                prev.next = first
            prev = second
            if second.next and second.next.next:
                first = second.next.next
                second = second.next
            else:
                break

        return og if og else head