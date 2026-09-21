# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        unique = set([n.val for n in nodes])
        res = None
        def po(n):
            nonlocal res
            if not n:
                return 0
            total  = po(n.left) + po(n.right) +( n.val in unique)
            if total == len(unique) and not res:
                res = n
            return total
        po(root)
        return res
            

