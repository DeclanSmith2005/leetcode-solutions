"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        res = 0
        def dfs(n, length):
            nonlocal res
            if not n:
                return 0
            heap = []
            for nbr in n.children:
                heapq.heappush(heap, -dfs(nbr, 1+length))
            a = -heapq.heappop(heap) if heap else 0
            b = -heapq.heappop(heap) if heap else 0
            res = max(a+b, a+length, b+length, res)
            return a + 1
        dfs(root, 0)
        return res

            
