# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        reversedNodes = []
        curr = None
        ptr = head
        while ptr != None:
            reversedNodes.append(ptr)
            ptr = ptr.next
        
        ptr = head
        while ptr != None and ptr.next != None:
            if len(reversedNodes) ==0:
                return head
            curr = reversedNodes.pop()
            if len(reversedNodes) > 0:
                reversedNodes[-1].next = None
            temp = ptr.next
            ptr.next = curr
            ptr = ptr.next
            ptr.next = temp
            ptr = ptr.next
        return head
        