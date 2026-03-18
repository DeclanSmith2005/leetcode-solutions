# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = 0
        def postOrder(node):
            nonlocal res
            if not node:
                return 0, 0
            contributors = 1
            total = node.val
            lt, lc = postOrder(node.left)
            rt, rc = postOrder(node.right)
            total = total + lt + rt
            contributors = contributors + rc + lc
            res = max(total / contributors, res)
            return total, contributors
        postOrder(root)
        return res