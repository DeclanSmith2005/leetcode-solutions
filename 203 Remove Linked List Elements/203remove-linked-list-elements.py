# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        root = ListNode(next = head)
        ptr, prev = head, root
        while ptr:
            if ptr.val == val:
                ptr = ptr.next
                prev.next = ptr
            else:
                prev = ptr
                ptr = ptr.next
        return root.next
                   