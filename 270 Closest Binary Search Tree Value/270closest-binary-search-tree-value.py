# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        minDifVal = float('inf')
        def postOrder(node):
            nonlocal minDifVal
            if not node:
                return
            postOrder(node.left)
            if abs(minDifVal- target) > abs(node.val - target):
                minDifVal = node.val
            postOrder(node.right)
        postOrder(root)
        return minDifVal