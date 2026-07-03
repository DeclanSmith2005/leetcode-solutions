class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        # memo stores the minimum cost it takes to travel from n to dest
        adj = defaultdict(list)
        if not edges:
            return -1
        for a, b, c in edges:
            if online[a] and online[b]:
                adj[a].append((b, c))

        def check(floor):
            # memo[n] represents the minimum cost of travelling from n to the destination
            memo = [None] * len(online)
            def dfs(n):
                if memo[n] is not None:
                    return memo[n]
                if n == len(online)-1:
                    return 0
                res = float('inf')
                for nxt, c in adj[n]:
                    if c >= floor:
                        res = min(res, c + dfs(nxt))
                memo[n] = res
                return memo[n]
            return dfs(0) <= k 

        l, r = -1, max(edges, key = lambda x: x[2])[2] 
        while l < r:
            m = (l + r + 1) // 2
            if check(m):
                l = m
            else:
                r = m - 1

        return l

            




                