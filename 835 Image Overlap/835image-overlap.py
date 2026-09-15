class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n, m = len(A[0]), len(A)
        res = 0
        def check(dx, dy):
            total = 0 
            row_range = range(max(0, -dy), min(m, m - dy))
            col_range = range(max(0, -dx), min(n, n - dx))
            for r in range(m):
                for c in range(n):
                    if 0 <= r + dy <= len(A)-1 and 0<= c + dx <= len(A[0])-1:
                        total += A[r+dy][c+dx] == B[r][c] and B[r][c] == 1
            return total
        for dx in range(-n, n):
            for dy in range(-m, m):
                res = max(res, check(dx, dy))
        return res