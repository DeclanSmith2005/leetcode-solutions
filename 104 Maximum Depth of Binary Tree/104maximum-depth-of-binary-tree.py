# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def inOrder(node, depth):
            if not node:
                return depth
            return 1+ max(inOrder(node.left, depth), inOrder(node.right, depth))
        return inOrder(root, 0)