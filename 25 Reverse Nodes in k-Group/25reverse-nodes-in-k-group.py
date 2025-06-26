
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr = head
        entrance = None
        first = False
        end  = None
        while True:
            start = ptr
            for i in range(k):
                if ptr != None:
                    ptr = ptr.next
                else:
                    entrance.next = start
                    return head
            ptr = start
            prev = None
            if entrance == None:
                first = True
            else:
                first = False
            for i in range (k):
                nex = ptr.next
                ptr.next = prev 
                prev = ptr
                if i == 0:
                    end = ptr
                ptr = nex
            if entrance != None:
                entrance.next = prev
            entrance = end 
            if first == True:
                head = prev
        
        return head

            
                

            

        