# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def postOrder(node):
            if not node:
                return 1
            l, r = postOrder(node.left), postOrder(node.right)
            if abs(l - r) > 1 or l == 0 or r == 0:
                return 0
            else:
                return max(l, r) + 1
        return postOrder(root) != 0