class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def setRow(row, matrix):
            for i in range(len(matrix[0])):
                if matrix[row][i]!= 0:
                    matrix[row][i] = None

        def setCol(col, matrix):
            for i in range(len(matrix)):
                if matrix[i][col]!=0:
                    matrix[i][col] = None

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    setRow(i, matrix)
                    setCol(j, matrix)
     
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==None:
                    matrix[i][j]=0