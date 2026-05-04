# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0

        def postOrder(node): # (run, lenths), (next, Values) 
            nonlocal res
            if not node:
                return (0,0)
            inc, dec = 1, 1
            if node.left:
                l = postOrder(node.left)
                if node.val == node.left.val + 1:
                    inc = l[0] + 1
                elif node.val == node.left.val -1:
                    dec = l[1] + 1
            if node.right:
                r = postOrder(node.right)
                if node.val == node.right.val + 1:
                    inc = max(inc, r[0] + 1)
                elif node.val == node.right.val -1:
                    dec = max(dec, r[1] + 1)
            res = max(res, inc + dec -1)
            return inc, dec
        postOrder(root)
        return res



            