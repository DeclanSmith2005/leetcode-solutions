class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottingCells = set()
        freshCells = set()
        dirs = [(1, 0), (0,1),(-1, 0),(0,-1)]

        def rot(row, col):
            return 0<= row < len(grid) and 0<= col < len(grid[0]) and (row, col) in freshCells
                
            
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] ==1:
                    freshCells.add((row, col))
                elif grid[row][col] == 2:
                    rottingCells.add((row, col))
        time = 0 
        while len(freshCells) > 0:
            orgf, orgr = len(freshCells), len(rottingCells)
            nxt = set()

            for r, c in rottingCells:
                for dr, dc in dirs:
                    if rot(r + dr, c + dc):
                        nxt.add((r + dr, c + dc))
            for pos in nxt:
                if pos in freshCells:
                    freshCells.remove(pos)
                rottingCells.add(pos)

            if (len(freshCells), len(rottingCells)) == (orgf, orgr):
                return -1
            time+=1
        return time
            

            
                
            