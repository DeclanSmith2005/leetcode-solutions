# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        po = []
        io = []
        def dfs(l, r):
            if l and r:
                return l.val == r.val and dfs(l.right, r.left) and dfs(r.right, l.left)
            return l == r
        
        return dfs(root.left, root.right)

            

            