# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(n, total):
            if not n:
                return False
            if total + n.val == targetSum and not n.left and not n.right:
                return True
            return dfs(n.left, total + n.val) or dfs(n.right, total + n.val)
        
        return dfs(root, 0)

            