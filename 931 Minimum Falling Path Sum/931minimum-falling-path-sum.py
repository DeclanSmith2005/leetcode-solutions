class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        memo = {} 

        def dp (r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            if r == len(matrix)-1:
                return matrix[r][c]
            if c == 0:
                memo[(r, c)] = min(dp(r+1, c), dp(r+1, c+1)) +matrix[r][c]
                return min(dp(r+1, c), dp(r+1, c+1)) +matrix[r][c]
            if c == len(matrix)-1:
                memo[(r, c)] = min(dp(r+1, c), dp(r+1,c-1))+ matrix[r][c]
                return min(dp(r+1, c), dp(r+1,c-1))+ matrix[r][c]
            memo[(r, c)] = min(dp(r+1, c+1), dp(r+1, c), dp(r+1, c-1))+ matrix[r][c]
            return min(dp(r+1, c+1), dp(r+1, c), dp(r+1, c-1))+ matrix[r][c]
        
        return min(dp(0, i) for i in range(len(matrix[0])))