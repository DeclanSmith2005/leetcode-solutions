# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        def preOrder(n):
            if not n:
                return None
            res.append(n)
            preOrder(n.left)
            preOrder(n.right)
        
        preOrder(root)

        for i in range(len(res)):
            res[i].right = res[i+1] if i < len(res)-1 else None
            res[i].left = None
        return root
            