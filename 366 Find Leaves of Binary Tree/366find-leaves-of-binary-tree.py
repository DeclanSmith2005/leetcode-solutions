# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def find(node):
            nonlocal res
            if not node.left and not node.right:
                res[-1].append(node.val)
                return True
            if node.left:
                find(node.left)
            if node.right:
                find(node.right)
        def prune(node):
            nonlocal root
            if not node.left and not node.right:
                if node == root:
                    root = None
                return 0
            if node.left:
                if prune(node.left) == 0:
                    node.left = None
            if node.right:
                if prune(node.right) == 0:
                    node.right = None
            return 1

        while root:
            res.append([])
            find(root)
            prune(root)
        return res
                