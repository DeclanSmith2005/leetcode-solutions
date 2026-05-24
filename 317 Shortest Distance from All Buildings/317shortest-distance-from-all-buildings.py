class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # mark all bulidings
        # exlore outward to all 0s, placing cumulative distance from building to the open spot
        dirs = [(0,1), (1,0), (0, -1), (-1, 0)]
        access = defaultdict(int)
        distance = defaultdict(int)
        buildings = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    buildings.add((r, c))

        for row, col in buildings:
            seen = {(row, col)}
            q= deque([(row, col, 0)])
            while q:
                r, c, dist = q.popleft()
                if grid[r][c] == 0:
                    access[(r, c)] += 1
                    distance[(r, c)]+= dist
                for dr, dc in dirs:
                    if (r + dr, c + dc) not in seen and r+dr >= 0 and r+dr < len(grid) and c + dc >= 0 and c + dc < len(grid[0]) and grid[r+dr][c+dc] == 0:
                        q.append((r+ dr, c + dc, dist +1))
                        seen.add((r + dr, c + dc))
    
        ans = float('inf')
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    if access[(r, c)] == len(buildings):
                        ans = min(ans, distance[(r, c)])
        
        return -1 if ans == float('inf') else ans


        