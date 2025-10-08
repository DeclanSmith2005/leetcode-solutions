class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        triangle[1][0] += triangle[0][0]
        triangle[1][1] += triangle[0][0]
        if len(triangle) == 2:
            return min(triangle[1][0], triangle[1][1])

        for row in range(2, len(triangle)-1):
            triangle[row][0] += triangle[row-1][0]
            triangle[row][row] += triangle[row-1][row-1]
            for i in range(1, len(triangle[row]) -1):
                triangle[row][i] += min (triangle[row-1][i], triangle[row-1][i-1])
        minimum = float('inf')
        for i in range(1, len(triangle[-1]) -1):
            minimum = min(minimum, (triangle[-1][i] + min(triangle[-2][i], triangle[-2][i-1])))
        minimum = min(minimum, triangle[-1][0] + triangle[-2][0])
        minimum = min(minimum, triangle[-1][-1] + triangle[-2][-1])
        return minimum