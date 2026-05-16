class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(-1,0), (1, 0), (0, -1), (0,1)]
        res = 0
        def destroy(r, c):
            if r < 0 or r > len(grid)-1 or c < 0 or c > len(grid[0])-1 or grid[r][c] == '0':
                return
            grid[r][c] = "0" 
            for dr, dc in dirs:
                destroy(r + dr, c + dc)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    res += 1
                    destroy(r, c)
        
        return res
