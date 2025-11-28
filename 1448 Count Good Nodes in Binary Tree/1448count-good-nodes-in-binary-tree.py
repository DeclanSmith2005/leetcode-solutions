# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def preOrder(node, prev):
            res = 0
            if not node:
                return 0
            if prev == None or prev <= node.val:
                prev = node.val
                res = 1
            res += preOrder(node.left, prev) + preOrder(node.right, prev)
            return res
        return preOrder(root, None)
            