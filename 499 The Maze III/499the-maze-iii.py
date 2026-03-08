class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        dirs = {'d':(1,0),  'l':(0,-1), 'r':(0,1), 'u':(-1, 0)}
        best = [[(float('inf'), "") for i in range(len(maze[0]))] for i in range(len(maze))]
        heap = [(0, *ball, [])]

        def nextLocations(r, c):
            res = []
            ir, ic = r, c
            for direction, (dr, dc) in dirs.items():
                while 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != 1:
                    r, c  = r + dr, c + dc
                    if (r - dr, c-dc) == tuple(hole):
                        break
                r, c = r - dr, c - dc
                if (r,c) != (ir, ic):
                    res.append((r, c, abs(ir - r) + abs(ic - c), direction))
                r, c = ir, ic
            return res
                
        while heap:
            print(heap)
            dist, row, col, prev = heapq.heappop(heap)
            if dist > best[row][col][0]:
                continue
            if (row, col) == tuple(hole):
                res = prev
                shortest = dist
            for r, c, d, direction in nextLocations(row, col):
                new = prev[:] + [direction]
                if ((dist + d, new) < best[r][c]):
                    best[r][c] = (dist + d, new)
                    heapq.heappush(heap, (dist + d, r, c, new))
        return "".join(best[hole[0]][hole[1]][1]) if  best[hole[0]][hole[1]][0] < float('inf') else "impossible"

                    

                

