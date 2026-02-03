# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        check = {}
        check2 = {}
        def dfs(node, dic):
            if not node:
                return
            dfs(node.left, dic)
            dfs(node.right, dic)
            dic[node.val] = target - node.val
        
        dfs(root1, check)
        dfs(root2, check2)

        for i in check.keys():
            if check[i] in check2:
                return True
        return False