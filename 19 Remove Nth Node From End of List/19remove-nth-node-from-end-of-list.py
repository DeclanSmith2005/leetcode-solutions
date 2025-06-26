# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        myMap = {}
        ptr = head
        i = 0 
        while True:
            if ptr == None:
                if i-n-1 >= 0:
                    get = myMap[i-n-1]
                    if get.next.next != None:
                        get.next = get.next.next
                    else:
                        get.next = None
                else:
                    head = head.next
                return head
            myMap[i] = ptr
            ptr = ptr.next
            i+=1
