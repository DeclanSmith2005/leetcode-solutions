# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0 
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, count, l))
                count+=1
        head =ptr = ListNode()
        while heap:
            val, count, l = heapq.heappop(heap)
            ptr.next = l
            ptr = ptr.next
            if l.next:
                l = l.next
                heapq.heappush(heap, (l.val, count, l))
        return head.next