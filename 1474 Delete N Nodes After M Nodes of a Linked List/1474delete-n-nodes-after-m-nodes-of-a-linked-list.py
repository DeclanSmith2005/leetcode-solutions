# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        a= b =head
        while b:
            i = 0
            while b and i < m-1:
                i+=1
                a = b = b.next
            i = 0
            while b and i < n+1:
                i+=1
                b = b.next
            if a:
                a.next = b
                a = a.next
        return head
