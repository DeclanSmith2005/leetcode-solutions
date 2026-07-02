class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # explore full dfs tree with a seen set, exiting early if we find somewhere in dp where we already visited with higher health 
        dp = defaultdict(int)
        dirs = [(0, 1), (1, 0), (-1,0), (0,-1)]
        seen = set()
        def dfs(r, c , h, seen):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r, c) in seen:
                return False
            if grid[r][c] == 1:
                h -= 1
            if h <= 0:
                return False
            if h <= dp[(r, c)]:
                return False
            if (r, c) == (len(grid)-1, len(grid[0])-1):
                return True
            dp[(r, c)] = h
            seen.add((r, c))
            for dr, dc in dirs:
                if dfs(r + dr, c + dc, h, seen):
                    return True
            seen.remove((r, c))
            return False

        return dfs(0, 0, health, set())