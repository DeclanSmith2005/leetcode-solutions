# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)
        def pre(n):
            if not n:
                return
            if n.left:
                adj[n].append(n.left)
                adj[n.left].append(n)
            if n.right:
                adj[n].append(n.right)
                adj[n.right].append(n)
            pre(n.left)
            pre(n.right)
        pre(root)
        seen = set()
        res = []
        def dfs(n, dist):
            if n in seen:
                return
            seen.add(n)
            if dist == k:
                res.append(n.val)
                return
            for nbr in adj[n]:
                if nbr not in seen:
                    dfs(nbr, dist + 1)
        dfs(target, 0)
        return res