class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0,-1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return sum(dfs(r + dr, c +dc) for dr, dc in dirs) + 1
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res = max(res, dfs(r, c))
        return res