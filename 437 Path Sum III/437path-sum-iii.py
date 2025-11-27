# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        prefixCounts = defaultdict(int)
        def preOrder(node, total):
            if not node:
                return 0 
            curr = total + node.val
            res = prefixCounts[(curr)-targetSum]

            prefixCounts[curr] += 1
            res += preOrder(node.left, curr)
            res += preOrder(node.right, curr)
            prefixCounts[curr]-= 1

            return res
        prefixCounts[0] = 1
        return preOrder(root, 0)

        
            

            