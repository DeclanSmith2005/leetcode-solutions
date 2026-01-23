# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 1
            if not (node.left or node.right):
                res += 1
                return 1
            l, r = dfs(node.left), dfs(node.right)
            if l and r:
                check = [node.val]
                if node.left:
                    check.append(node.left.val)
                if node.right:
                    check.append(node.right.val)
                if all(element == check[0] for element in check):
                    res += 1
                    return 1
                else: 
                    return 0
        dfs(root)
        return res
            

            