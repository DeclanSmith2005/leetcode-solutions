class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def roll(i, j, di, dj):
            ni, nj = i, j
            while 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and maze[ni][nj] != 1:
                ni += di
                nj += dj
            return ni - di, nj - dj

        def dfs(i, j):
            if (i, j) in visited:
                return 0
            visited.add((i, j))
            if [i, j] == destination:
                return 1
            return max([dfs(*roll(i, j, di, dj)) for di, dj in dirs])
        
        return dfs(*start) == 1
            

            

            


            
