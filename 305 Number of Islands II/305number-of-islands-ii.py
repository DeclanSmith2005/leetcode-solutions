from typing import List

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = [-1] * (m * n)   # -1 means water (not in DSU)
        rank = [0] * (m * n)
        count = 0
        res = []
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def idx(r, c):
            return r * n + c

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(a, b):
            nonlocal count
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            # union by rank
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            count -= 1

        for r, c in positions:
            p = idx(r, c)
            if parent[p] != -1:          # duplicate add
                res.append(count)
                continue

            parent[p] = p               # add land
            rank[p] = 0
            count += 1

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    q = idx(nr, nc)
                    if parent[q] != -1:  # neighbor is land
                        union(p, q)

            res.append(count)

        return res
