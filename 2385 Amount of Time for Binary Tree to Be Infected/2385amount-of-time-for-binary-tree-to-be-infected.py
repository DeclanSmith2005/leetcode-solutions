# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)
        def pre(n):
            if not n:
                return
            if n.left:
                adj[n.val].append(n.left.val)
                adj[n.left.val].append(n.val)
            if n.right:
                adj[n.val].append(n.right.val)
                adj[n.right.val].append(n.val)
            pre(n.left)
            pre(n.right)
        pre(root)
        q = deque([start])
        res = -1
        seen = set([start])
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                for nbr in adj[curr]:
                    if nbr not in seen:
                        seen.add(nbr)
                        q.append(nbr)
            res+= 1
        return res


