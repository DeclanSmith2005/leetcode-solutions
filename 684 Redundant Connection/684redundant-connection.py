class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[b].append(a)
            adj[a].append(b)

        def dfs(n, seen, parent, barred):
            if n in seen:
                return True
            seen.add(n)
            for nbr in adj[n]:
                if (n, nbr) == barred or (nbr, n) == barred or nbr == parent:
                    continue
                if nbr in seen or dfs(nbr, seen, n, barred):
                    return True
            return False

        for i in range(len(edges)-1, -1,  -1):
            a, b = edges[i]
            if len(adj[a]) == 1 or len(adj[b]) == 1:
                continue
            seen = set()
            if not any(dfs(node, seen, None, (a, b)) for node in range(len(edges)) if node not in seen):
                return (a, b)


            


            