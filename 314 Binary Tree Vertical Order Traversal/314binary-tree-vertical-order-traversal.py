# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        column = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, col = q.popleft()
            column[col].append(node.val)
            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))
        cols = sorted(column.keys())
        res = []
        for c in cols:
            res.append(column[c])
        return res