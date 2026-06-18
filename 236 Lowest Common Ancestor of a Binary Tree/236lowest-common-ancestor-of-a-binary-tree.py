# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def postOrder(n):
            if not n:
                return None
            if n == p or n == q:
                return n 
            l, r = postOrder(n.left), postOrder(n.right)
            if l and r:  
                return n
            if l:
                return l
            if r:
                return r
        return postOrder(root)
