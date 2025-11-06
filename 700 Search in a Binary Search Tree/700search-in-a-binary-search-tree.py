# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ptr = root
        while True:
            if ptr == None:
                return None
            if val < ptr.val:
                ptr = ptr.left
            elif val > ptr.val:
                ptr = ptr.right
            elif val == ptr.val:
                return ptr
            else:
                return None