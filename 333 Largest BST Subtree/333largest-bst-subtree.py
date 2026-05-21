# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        curr = float('-inf')
        def validate(n):
            nonlocal curr
            if not n:
                return True
            if not validate(n.left) or n.val <= curr:
                return False
            curr = n.val 
            if not validate(n.right):
                return False
            return True

        def size(n):
            if not n:
                return 0
            l = size(n.left)
            r= size(n.right)
            return l + r + 1

        def ino(n):
            nonlocal curr
            if not (n):
                return 0
            curr = float('-inf')
            if validate(n):
                return size(n)
            return max(ino(n.left), ino(n.right))
            
        return ino(root)
           
            
            