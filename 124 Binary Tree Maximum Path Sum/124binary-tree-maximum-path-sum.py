# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def post(n):
            nonlocal res
            if not n:
                return 0 
            l = max(0, post(n.left))
            r = max(0, post(n.right))
            res = max(res, n.val + l + r)
            return max(n.val + l, n.val + r)
        post(root)
        return res