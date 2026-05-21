# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr = float("-inf")
        def ino(n):
            nonlocal curr
            if not n:
                return True
            if not ino(n.left) or n.val <= curr:
                return False
            curr = n.val 
            if not ino(n.right):
                return False
            return True
        return ino(root)
            




    """
        ret = [True]
        if root == None:
            return False
        last = None
        def inOrder(node):
            nonlocal last
            if node == None:
                return 
            inOrder(node.left)
            curr = node.val
            if last != None:
                if last >= curr:
                    ret[0] = False
            last = curr
            inOrder(node.right)
        inOrder(root)
        return ret[0]
    """