# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def pre(n, total):
            if not n:
                return 
            total = (total * 10 )+ n.val
            if not n.left and not n.right:
                res.append(total)
            pre(n.left, total)
            pre(n.right, total)
        pre(root, 0)
        return sum(res)