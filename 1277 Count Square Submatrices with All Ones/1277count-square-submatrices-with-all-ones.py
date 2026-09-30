class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        
        for c in range(len(matrix[0])):
            dp[0][c] = matrix[0][c]
        
        for r in range(len(matrix)):
            dp[r][0] = matrix[r][0]
        
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    continue
                dp[r][c] = min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]) + 1

        return sum([sum(dp[r]) for r in range(len(dp))])
