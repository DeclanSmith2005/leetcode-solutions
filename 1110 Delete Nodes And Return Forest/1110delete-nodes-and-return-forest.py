# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        temp = []
        res = [] if root.val in to_delete else [root]

        def preOrder(node):
            if not node:
                return None
            node.left, node.right = preOrder(node.left), preOrder(node.right)
            if node.val in to_delete:
                temp.extend([node.left, node.right])
                return None
            return node

        preOrder(root)
        for r in temp:
            if r:
                res.append(r)
        return res
        
                
