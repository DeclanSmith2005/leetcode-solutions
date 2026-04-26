# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        def preOrder(node, prev, length):
            if not node:
                return 0
            length = length + 1 if prev != None and node.val == prev.val +1 else 1
            return max(length, max(preOrder(node.left, node, length),
                                   preOrder(node.right, node, length)))
                
        return preOrder(root, None, 0)
            
            
            