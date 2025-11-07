class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        res = 0 
        for row in grid:
            rows[tuple(row)] += 1 
        for col in range(len(grid[0])):
            key = tuple(grid[i][col] for i in range(len(grid[0])))
            res+= rows.get(key, 0)
        return res