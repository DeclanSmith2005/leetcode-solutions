# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        res = []
        memo = defaultdict(list)
        def create(s, e):
            if s > e:
                return [None]
            if (s, e) in memo:
                return memo[(s, e)]
            
            for i in range(s, e+1):
                left = create(s, i-1)
                right = create(i+1, e)
            
                for l in left:
                    for r in right:
                        curr = TreeNode(i, l, r)
                        memo[(s, e)].append(curr)
            return memo[(s, e)]
        
        return create(1, n)
                    


