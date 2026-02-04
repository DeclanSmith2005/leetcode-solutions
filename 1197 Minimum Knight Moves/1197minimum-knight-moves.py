class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        ans = (abs(x),abs(y))
        q = deque([(0,0,0)])
        seen = set()
        moves = [(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2)]
        while q:
            x,y,c = q.popleft()
            if x == ans[0] and y == ans[1]:
                return c
            for dx, dy in moves:
                if (x+dx, y+dy) not in seen and x+dx >= -1 and y+dy>= -1:
                    q.append((x+dx, y+dy, c+1))
                    seen.add((x+dx, y+dy))