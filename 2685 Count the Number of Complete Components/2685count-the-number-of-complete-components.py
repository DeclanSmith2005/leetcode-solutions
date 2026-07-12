class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [ i for i in range(n)]
        rank = [1 for i in range(n)]
        adj = defaultdict(list)
        # union all guys in the egdes array
        # since a nodes connections must be within the same component (because we union all its edges) we just check for each guy if the length of its adjacency is the same as the rank of its parent. if true for all nodes of a component, thats a complete component 
        def find(a):
            while parents[a] != a:
                a = parents[a]
            return a
            
        def union(a, b):
            p1, p2 = find(a), find(b)
            if p2 == p1:
                return
            if rank[p1] < rank[p2]:
                parents[p1] = p2
                rank[p2] += rank[p1]
                rank[p1] = 0
            else:
                parents[p2] = p1
                rank[p1] += rank[p2]
                rank[p2] = 0

        for a, b in edges:
            union(a, b)
            adj[a].append(b)
            adj[b].append(a)
        
        nonconnected = set()
        pset = set()
        for i in range(n):
            p = find(i)
            pset.add(p)
            if len(adj[i]) != rank[p]-1:
                nonconnected.add(p)
                
        return len(pset - nonconnected)
        

