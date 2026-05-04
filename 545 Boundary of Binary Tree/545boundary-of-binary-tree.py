# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        l, r, leaves = [], [], []
        if root.left:
            curr = root.left
            while curr.left or curr.right:
                l.append(curr.val)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
        if root.right:
            curr = root.right
            while curr.left or curr.right:
                r.append(curr.val)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left 
        
        def inOrder(node):
            if not node:
                return 
            inOrder(node.left)
            if not ( node.left or node.right) and node != root:
                leaves.append(node.val)
            inOrder(node.right)
        inOrder(root)
        return [root.val] + l + leaves + r[::-1]
            