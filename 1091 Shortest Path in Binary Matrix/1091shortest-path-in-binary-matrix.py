class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque([[0, 0, 1]]) if grid[0][0] == 0 else []
        dirs = ([-1,-1], [1, 0], [-1, 1], 
                [0, -1],         [0, 1],
                [1, -1], [-1, 0], [1, 1])

        seen = set([(0, 0)])
        res = None
        while q:
            r, c, dist = q.popleft()
            if (r, c) == (len(grid)-1, len(grid)-1):
                res = dist
            for dr, dc in dirs:
                nr, nc = (r + dr, c + dc)
                if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid) or grid[nr][nc] == 1 or (nr, nc) in seen:
                    continue
                q.append([nr, nc, dist+1])
                seen.add((nr, nc))
        
        return res if res else -1
