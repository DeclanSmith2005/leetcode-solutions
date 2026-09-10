# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def io(n, curr):
            if not n:
                return 
            curr.append(n.val)
            if not n.left and not n.right and sum(curr) == targetSum:
                res.append(curr[:])
            io(n.left, curr); io(n.right, curr)
            curr.pop()

        io(root, [])
        return res

            
