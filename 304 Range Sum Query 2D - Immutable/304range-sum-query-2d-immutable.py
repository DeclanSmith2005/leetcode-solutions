class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
        self.dp[1][1] = matrix[0][0]
        for r in range(1, len(matrix)):
            self.dp[r+1][1] = self.dp[r][1] + matrix[r][0]
        for c in range(1, len(matrix[0])):
            self.dp[1][c+1] = self.dp[1][c] + matrix[0][c]
        for r in range(2, len(matrix)+1):
            for c in range(2, len(matrix[0])+1):
                self.dp[r][c] = matrix[r-1][c-1] + self.dp[r-1][c] + self.dp[r][c-1] - self.dp[r-1][c-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1; col1+= 1; row2 += 1; col2 += 1
        return self.dp[row2][col2] - self.dp[row1-1][col2] - self.dp[row2][col1 -1] + self.dp[row1-1][col1-1] 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)