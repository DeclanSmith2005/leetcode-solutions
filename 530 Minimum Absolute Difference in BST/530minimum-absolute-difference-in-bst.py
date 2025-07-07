# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minDif = float('inf')
        ptr = root
        last = None
        def inOrderTraversal(node):
            nonlocal minDif
            nonlocal last
            if node == None:
                return None
            inOrderTraversal(node.left)
            curr = node.val
            if last!= None:
                minDif = min(minDif, curr-last)
            last = curr
            inOrderTraversal(node.right)
        inOrderTraversal(root)
        return minDif
