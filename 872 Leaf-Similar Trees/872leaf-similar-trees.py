# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def inOrder(node, curr):
            if node:
                inOrder(node.left, curr)
                if not (node.left or node.right):
                    curr.append(node.val)
                inOrder(node.right, curr)
            return curr
        return inOrder(root1, []) == inOrder(root2, [])