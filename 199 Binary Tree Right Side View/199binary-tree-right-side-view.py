# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        curr = [root]
        nextRow = []
        if root == None:
            return []
        retList = [root.val]
        while True:
            for node in curr:
                if node.left:
                    nextRow.append(node.left)
                if node.right:
                    nextRow.append(node.right)
            curr = nextRow
            nextRow = []
            if curr == []:
                return retList
            retList.append(curr[len(curr)-1].val)

                
