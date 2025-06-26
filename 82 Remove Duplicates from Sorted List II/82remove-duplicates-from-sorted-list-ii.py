# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        adder = newHead
        one = head
        if head == None or head.next == None:
            return head
        two = head.next
        if one.val != two.val:
            adder.next = one
            adder = adder.next
        while (two != None):
            while ( two != None and two.val == one.val ):
                two = two.next
                one = one.next
            if two == None:
                adder.next = None
                return newHead.next
            if two.next != None:
                two = two.next
                one = one.next
            else:
                adder.next = two
                return newHead.next
            if (two.val == one.val):
                continue
            else:
                adder.next = one
                adder = adder.next
        
        return newHead.next

            
            

            

        

