# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        ptr = head
        length = 1
        while ptr.next!= None:
            ptr = ptr.next
            length +=1
        ptr.next = head
        for i in range(length-(k%length)-1):
            head = head.next
        temp = head.next
        head.next = None
        return temp
        