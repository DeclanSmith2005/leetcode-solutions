# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def size(n):
            if not n:
                return 0
            l = size(n.left)
            r= size(n.right)
            return l + r + 1
        return size(root)