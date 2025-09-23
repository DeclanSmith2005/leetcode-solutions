# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list2.val < list1.val:
            temp = list1
            list1 = list2
            list2 = temp
        ptr1 = list1
        ptr2 = list2

        while ptr2 != None and ptr1.next != None:
            if ptr1.next.val < ptr2.val:
                ptr1 = ptr1.next
                continue
            else:
                temp = ptr1.next
                ptr1.next = ptr2
                ptr2 = ptr2.next
                ptr1 = ptr1.next
                ptr1.next = temp

        
        if ptr2  == None:
            return list1
        ptr1.next = ptr2
        return list1

        
