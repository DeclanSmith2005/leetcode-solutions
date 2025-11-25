# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = evenHead =ListNode()
        oddHead = odd = ListNode()
        ptr = head 
        flag = True
        while ptr!= None:
            if flag: 
                odd.next = ptr
                odd = odd.next
            else:
                even.next = ptr
                even = even.next
            flag = not flag
            ptr = ptr.next
        even.next = None
        odd.next = evenHead.next
        return oddHead.next
            