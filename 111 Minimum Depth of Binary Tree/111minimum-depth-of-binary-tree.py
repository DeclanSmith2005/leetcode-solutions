# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def  post(n, height):
            if not n:
                return float('inf')
            if not (n.left or n.right):
                return height
            return min(post(n.left, height+1), post(n.right, height + 1))
        return post(root, 1)

