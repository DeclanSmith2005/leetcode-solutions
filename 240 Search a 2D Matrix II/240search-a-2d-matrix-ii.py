class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix)-1, 0
        while c <= len(matrix[0])-1 and r >= 0:
            if matrix[r][c] < target:
                c +=1
            elif matrix[r][c] > target:
                r -=1
            else:
                return True
        return False
