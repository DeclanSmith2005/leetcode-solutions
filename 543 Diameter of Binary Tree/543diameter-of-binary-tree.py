# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def preOrder( node):
            nonlocal res
            if not node:
                return -1
            curr = (1+ preOrder(node.left), 1+ preOrder(node.right))
            res = max(res, curr[0] + curr[1])
            return max(curr[0], curr[1])
        preOrder(root)
        return res