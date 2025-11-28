# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        rHead = None
        ptr = head
        length = 0
        while ptr:
            rHead = ListNode(ptr.val)
            rHead.next = prev
            prev = rHead
            ptr = ptr.next
            length +=1 

        res = float('-inf')
        ptr = head
        for i in range((length // 2)+1):
            res = max(res, ptr.val + rHead.val)
            ptr, rHead = ptr.next, rHead.next
        return res

