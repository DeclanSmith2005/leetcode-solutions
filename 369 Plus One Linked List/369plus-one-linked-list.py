# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # first reverse
        def rev(head):
            prev = None
            ptr = head
            while ptr:
                tmp = ptr.next
                ptr.next = prev
                prev = ptr 
                ptr = tmp
            return prev

        end = rev(head)
        ptr = end
        while ptr.next and ptr.val == 9:
            ptr.val = 0
            ptr = ptr.next
        if ptr.val == 9:
            ptr.next = ListNode(1)
            ptr.val = 0 
            ptr = ptr.next
        else:
            ptr.val += 1
        return rev(end)
        
        
        
        