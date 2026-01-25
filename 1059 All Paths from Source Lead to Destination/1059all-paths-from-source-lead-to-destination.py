class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        nbrs = defaultdict(list)
        for src, dst in edges:
            nbrs[src].append(dst)
            if src == destination:
                return False
        seen = set()
        memo = {}
        def dfs(node):
            if not nbrs[node]:
                return node == destination
            if node in seen:
                return False
            if node in memo:
                return memo[node]
            seen.add(node)
            for i in nbrs[node]:
                if not dfs(i):
                    memo[node] = False
                    return False
            seen.remove(node)
            memo[node] = True
            return True
        if len(edges) == 0:
            return destination == source
        return dfs(source)

