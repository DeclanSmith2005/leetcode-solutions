class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # store locations of all gates
        # for each gate dfs outwards style and dist = min (dist, dist to the currecntly explore gate)
        # kill dfs instances that land on nodes which already have a closer distance
        dirs = [(0,1), (1, 0), (-1,0), (0, -1)]
        gates = []
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    gates.append((r,c))
                    
        def dfs(r, c, dist):
            if dist > 0 and (r < 0 or r > len(rooms)-1 or c < 0 or c > len(rooms[0])-1 or rooms[r][c] <= dist):
                return 
            rooms[r][c] = dist
            for dr, dc in dirs:
                dfs(r+dr, c + dc, dist + 1)
        
        for r, c in gates:
            dfs(r, c, 0)
        
        

            


