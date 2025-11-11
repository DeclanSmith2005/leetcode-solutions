# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lead= lag = head
        while lead:
            while lead and lead.val == lag.val:
                lead = lead.next
            lag.next = lead
            lag = lead
        return head
        