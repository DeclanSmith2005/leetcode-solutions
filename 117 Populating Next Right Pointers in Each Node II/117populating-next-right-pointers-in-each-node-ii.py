"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = deque([root])
        while q:
            for i in range(len(q)-1):
                curr = q.popleft()
                curr.next = q[0]
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            last = q.popleft()
            if not last:
                continue
            last.next = None
            if last.left:
                q.append(last.left)
            if last.right:
                q.append(last.right)
        return root
    

