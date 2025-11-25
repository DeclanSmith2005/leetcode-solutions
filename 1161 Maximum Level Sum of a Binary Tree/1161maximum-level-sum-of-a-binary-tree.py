# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = []
        q = deque([root])
        level = 0
        while q:
            level +=1
            total = 0 
            for i in range(len(q)):
                curr = q.popleft()
                total += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append((total, level))
            
        return sorted(res, key=lambda x: (x[0], -x[1]))[-1][1]




        