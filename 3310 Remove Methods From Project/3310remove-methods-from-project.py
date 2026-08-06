class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # run union find and dfs from node k 
        # if size of connected component and dfs are not the same, then some non suspicous method must invoke a suspicious method, return no changes
        # otherwise, remove the dfs of children from k , and bang
        adj = defaultdict(list)
        seen = set()
        sus = set()
        res = []

        def dfs(n):
            if n in seen:
                return
            seen.add(n)
            sus.add(n)
            for nbr in adj[n]:
                dfs(nbr)
        
        for a, b in invocations:
            adj[a].append(b)

        dfs(k)
        
        for a, b in invocations:
            if a not in sus and b in sus:
                return [i for i in range(n)]

        for i in range(n):
            if i in sus:
                continue
            res.append(i)
        return res


        
        