# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if q.val < p.val:
            temp = q
            q = p
            p = temp
        def preOrder(node):
            if not node:
                return None
            if p.val<=node.val<=q.val:
                return node
            if node.val < p.val:
                return preOrder(node.right)
            if node.val > q.val:
                return preOrder (node.left)
        return preOrder(root)

            
            