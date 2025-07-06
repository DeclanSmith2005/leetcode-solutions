# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root == None:
            return []
        q = deque([root])
        retList = []
        while q:
            total = 0
            levelSize = len(q)
            for node in range(levelSize):
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                total+= node.val
            avg = total/levelSize
            retList.append(avg)
            
        return retList