class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        indicies = [0 for i in range(m)]
        minIndex, minIndexRow = 0, 0
        maxIndex, maxIndexRow = 0, 0
        minVal = float('inf')
        maxVal = max(mat[i][0] for i in range(m))
        while minIndex < n-1:
            minIndex = indicies[0]
            for r in range(m):
                while indicies[r] < n-1 and mat[r][indicies[r]] < maxVal:
                    indicies[r] += 1
                maxVal = max(maxVal, mat[r][indicies[r]])
                if r < minIndex:
                    minIndex, minIndexRow = indicies[r], r
                if r > maxIndex:
                    maxIndex, maxIndexRow = indicies[r], r
            if mat[minIndexRow][minIndex] == mat[maxIndexRow][maxIndex]:
                if minIndex != n-1:
                    return mat[0][indicies[0]]
                elif all(mat[r][indicies[r]] == mat[0][indicies[0]] for r in range(m)):
                    return mat[0][indicies[0]]
        return -1
           
                


                