"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        uniqueNodes = len(set(tree))
        childrenNum = {None: 0}
        check = set(tree)
        def dfs(node):
            total = 1
            if not node or node in childrenNum:
                return childrenNum[node]
            for child in node.children:
                total += dfs(child)
            childrenNum[node] = total
            return total
        for i in tree:
            if dfs(i) == uniqueNodes:
                return i
        

        