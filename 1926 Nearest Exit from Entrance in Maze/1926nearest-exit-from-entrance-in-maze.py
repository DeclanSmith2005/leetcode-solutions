class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque([tuple(entrance)])
        seen = set([tuple(entrance)])
        steps = 0
        options = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                if (row == 0 or row == len(maze)-1 or col == 0 or col == len(maze[0])-1) and (row, col) != tuple(entrance):
                    return steps
                for r, c in options:
                    r, c = r + row, c + col
                    if -1 < r < len(maze) and -1 < c < len(maze[0]) and maze[r][c] == '.' and (r,c) not in seen:
                        q.append((r, c))
                        seen.add((r, c))
            steps +=1
        return -1
            


            