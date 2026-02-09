from typing import List
import heapq

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        R, C = len(maze), len(maze[0])
        sr, sc = start
        tr, tc = destination

        def roll(r, c, dr, dc):
            steps = 0
            # move while NEXT cell is valid and empty
            while 0 <= r + dr < R and 0 <= c + dc < C and maze[r + dr][c + dc] == 0:
                r += dr
                c += dc
                steps += 1
            return r, c, steps

        INF = 10**18
        dist = [[INF] * C for _ in range(R)]
        dist[sr][sc] = 0

        heap = [(0, sr, sc)]  # (d, r, c)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            d, r, c = heapq.heappop(heap)
            if d != dist[r][c]:
                continue
            if (r, c) == (tr, tc):
                return d

            for dr, dc in dirs:
                nr, nc, steps = roll(r, c, dr, dc)
                nd = d + steps
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(heap, (nd, nr, nc))

        return -1
