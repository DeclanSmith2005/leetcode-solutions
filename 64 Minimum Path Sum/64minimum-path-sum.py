class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range( len(grid)):
            for col in range(len(grid[0])):
                if col == row == 0:
                    continue
                elif col == 0:
                    grid[row][col] += grid[row-1][col]
                elif row == 0:
                    grid[row][col] += grid[row][col-1]
                else:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        return grid[-1][-1]
                

