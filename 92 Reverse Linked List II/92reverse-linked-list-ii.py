# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        check = False
        entrance = None
        exits = None
        if left == right:
            return head
        i = 1
        while( curr.next != None):
            if i+1 == left:
                entrance = curr
            if i == left:
                exits = curr
            prev = None
            nex = ListNode()
            while i >= left and i <= right:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
                if left == 1:
                    head = prev
                check= True
                i+=1
            if check == True:
                if nex != None:
                    exits.next = nex
                if left > 1:
                    entrance.next = prev
                break
            else:
                i+=1
                curr = curr.next
        return head

        