class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[0])
        numArrows = 0
        end = points[0][1]
        for i in range(1, len(points)):
            end = min(end, points[i][1])
            if points[i][0] > end:
                numArrows+=1
                end = points[i][1]
        return numArrows+1