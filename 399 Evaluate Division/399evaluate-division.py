class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # topological sort on systems of equations to determine each variable, then solve queries
        graph = defaultdict(list)
        for i in range(len(values)):
            a, b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        def dfs(n, tgt, product, visited):
            if n == tgt:
                return product
            if n in visited:
                return -1
            visited.add(n)
            for nbr, m in graph[n]:
                res =  dfs(nbr, tgt, m*product, visited)
                if res != -1:
                    return res
            return -1
        ans = []
        for a, b in queries:
            ans.append(-1 if a== b and len(graph[a]) == 0 else dfs(a, b, 1, set()))
        return ans

