class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        dirs = [(1, 0 ), (-1 , 0), (0, 1), (0, -1)]
        def detect(r, c, tgt, path, t):
            if r < 0 or r > len(grid)-1 or c < 0 or c > len(grid[0])-1:
                return False
            if (r,c) in path:
                if path[(r,c)] <= t- 4:
                    return True
                else:
                    return False
            if grid[r][c] != tgt:
                return False
            grid[r][c] = None
            path[(r,c)] = t
            return any(detect(r + dr, c + dc, tgt, path, t+1) for dr, dc in dirs)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    if detect(r, c, grid[r][c], {}, 0):
                        return True
        return False



            