# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeTree(left, right):
            mid = (left + right)//2
            if right < left:
                return None
            node = TreeNode(nums[mid])
            node.right = makeTree(mid+1, right) 
            node.left = makeTree(left, mid-1)
            return node
        
        return makeTree(0, len(nums)-1)



