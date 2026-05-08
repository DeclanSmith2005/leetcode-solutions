class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0]* len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        for col in range(len(dp[0])):
            if obstacleGrid[0][col] != 1:
                dp[0][col] = 1 
            else:
                 break
        for row in range(len(dp)):
            if obstacleGrid[row][0] != 1:
                dp[row][0] = 1 
            else:
                break
        for row in range(1, len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[0])):
                print(row, len(dp))
                dp[row][col] = dp[row][col-1] + dp[row-1][col] if obstacleGrid[row][col] != 1 else 0
        return dp[-1][-1]
                
