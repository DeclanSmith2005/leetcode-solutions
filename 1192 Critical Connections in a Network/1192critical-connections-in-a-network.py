class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # key idea: any edge we find which is not part of a cycle is a critical connection
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
        disc = [0] * n
        low  = [0] * n 
        visited = set()
        time = 0 
        res = []
        def dfs(curr, prev):
            nonlocal time
            low[curr] = disc[curr] = time
            time+=1
            visited.add(curr)
            for nbr in adj[curr]:
                if nbr not in visited:
                    dfs(nbr, curr)
                    low[curr] = min(low[curr], low[nbr])
                elif nbr != prev:
                    low[curr] = min(low[curr], disc[nbr])
                if low[nbr] > disc[curr]:
                    res.append([nbr, curr])
        dfs(0, -1)
        return res

        
