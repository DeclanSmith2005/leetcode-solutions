class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        pattern = []
        def destroy(x,y, ox, oy):
            if x< 0 or x > len(grid[0])-1 or y < 0 or y > len(grid)-1 or grid[y][x] == 0:
                return
            grid[y][x] = 0
            pattern.append((x-ox, y-oy))
            for dx, dy in [(-1, 0),(1, 0),(0,-1),(0,1)]:
                destroy(x+dx, y+dy, ox, oy)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                destroy(col,row,col,row)
                islands.add(tuple(pattern)) if len(pattern) > 0 else None
                pattern = [] 
        res = 0
        return len(islands)
               