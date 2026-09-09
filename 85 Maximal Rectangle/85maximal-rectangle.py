class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # determine the max width of a rectangle in that row ending at that point. can compare with columns below to find the max width of a base ending at that. min of seen so far up the column is the width of that rectangle and hegiht is the height 
        res = 0
        width = [[0]*(len(matrix[0])+1) for i in range(len(matrix))]

        for r in range(len(matrix)):
            for c in range(1, len(matrix[0])+1):
                width[r][c] = width[r][c-1] + 1 if matrix[r][c-1] == '1' else 0
        
        for base in range(len(matrix)-1, -1, -1):
            for c in range(1, len(matrix[0])+1):
                if base < len(matrix)-1 and width[base][c] <= width[base+1][c]:
                        continue
                currWidth = float('inf')
                for r in range(base, -1, -1):
                    currWidth = min(currWidth, width[r][c])
                    res = max(res, currWidth * (base - r +1))
        return res

            