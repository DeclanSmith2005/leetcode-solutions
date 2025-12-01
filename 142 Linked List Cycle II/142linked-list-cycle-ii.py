# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        innodes = defaultdict(int)
        ptr = head
        while ptr:
            innodes[ptr] +=1
            if innodes[ptr] > 1:
                return ptr
            ptr =ptr.next
        return None
