class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def union(a, b):
            p1, p2 = find(a), find(b)
            if rank[p1] > rank[p2]:
                parents[p2] = parents[p1]
                rank[p1] += rank[p2]
            else:
                parents[p1] = parents[p2]
                rank[p2] += rank[p1]
        
        def find(a):
            while parents[a] != a:
                a = parents[a]
            return a
        
        for start, dest in edges:
            union(start, dest)

        return sum(parents[i] == i for i in range(n))
