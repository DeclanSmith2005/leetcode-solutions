class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = None
        
        def findRow():
            nonlocal matrix
            right = len(matrix)-1
            left = 0
            if len(matrix)==1:
                    return matrix[0]
            while ( left<= right):
                mid  = (right + left) // 2
                if mid == len(matrix)-1:
                    if matrix[mid][-1] < target:
                        return None
                    else:
                        return matrix[mid]
                if mid == 0:
                    if target < matrix[mid][0]:
                        return None
                if matrix[mid][0] <= target:
                    if matrix[mid+1][0] > target:
                        return matrix[mid]
                    else:
                        left = mid + 1
                else:
                    right = mid -1
        row = findRow()
        if row == None:
            return False
        
        right = len(row)-1
        left = 0
        if len(row) == 1:
            if target == row[0]:
                return True
            else:
                return False
        while ( left<= right):
            mid  = (right + left) // 2
            if row[mid] == target:
                return True
            if target < row[mid]:
                right  = mid -1
            else:
                left = mid +1
        return False
        
        