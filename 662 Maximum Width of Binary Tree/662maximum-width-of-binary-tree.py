# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left = {}
        right = {}
        maxDepth = 1
        res = 0
        def inorder(n, depth, pos):
            nonlocal maxDepth
            maxDepth = max(maxDepth, depth)
            if not n:
                return
            inorder(n.left, depth + 1, pos*2)
            left[depth]= min(left.get(depth, float('inf')), pos)
            right[depth] = max(right.get(depth, float('-inf')), pos)
            inorder(n.right, depth+1, (pos*2)+1)
        inorder(root, 0, 0)
        for i in range(maxDepth):
            res = max(res, right[i] - left[i] + 1)
        return res