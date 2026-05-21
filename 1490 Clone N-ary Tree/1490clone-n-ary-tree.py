"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        def dfs(n):
            if not n:
                return None
            cpy = Node(n.val)
            for node in n.children:
                cpy.children.append(dfs(node))
            return cpy
        return dfs(root)