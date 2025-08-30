class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # for row, col in the matrix: 
        #first put store the coordinates of all the ajacent 1s in the pocket. iterate from top left 1 through to the next most up and left, and bulid a square from it. whenever the next upmost leftmost ajacent guy doesn't fit into the sqaure we're buliding we can return, set everything we've processed to 0, and move onto the next guy in the set. processed guys are set to 0. continue for each pocket of 1s, and return the largest square.
        dp = [[0]*len(matrix[0]) for i in range(len(matrix))] 
        greatest = 0

        for i in range(len(matrix[0])):
            dp[0][i] = int(matrix[0][i])
            if  matrix[0][i] == "1":
                greatest = 1
        for i in range(len(matrix)):
            dp[i][0]= int(matrix[i][0])
            if  matrix[i][0] == "1":
                greatest = 1
        
        
        for row in range(1, len(matrix)):
            for col in range(1,len(matrix[0])):
                if matrix[row][col] == "0":
                    dp[row][col] = 0
                else:
                    dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1])+1
                greatest= max(greatest, dp[row][col])
        return greatest*greatest
