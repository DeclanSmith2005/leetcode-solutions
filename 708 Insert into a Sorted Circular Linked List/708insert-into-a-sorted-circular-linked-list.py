"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        if not head:
            new = Node(insertVal)
            new.next = new
            return new
        elif head.next == head:
            head.next = Node(insertVal, head)
            return head

        curr = head
        while curr.next != head:
            if (curr.val <= insertVal < curr.next.val):
                break
            if (insertVal <= curr.next.val or insertVal >= curr.val) and curr.next.val < curr.val:
                break
            curr = curr.next
        temp = curr.next
        curr.next = Node(insertVal, temp)
        return head