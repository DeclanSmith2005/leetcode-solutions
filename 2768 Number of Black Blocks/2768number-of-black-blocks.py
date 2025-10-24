class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        res = [0, 0, 0, 0, 0]
        dp = {}
        for row, col in coordinates:
            for newRow in range(row-1, row+1):
                for newCol in range(col-1, col+1):
                    if 0 <= newRow < m-1 and 0 <= newCol < n-1:
                        dp[(newRow, newCol)] = dp.get((newRow, newCol), 0) +1
        total = 0 
        for i in dp.values():
            total += 1
            res[i]+=1
        res [0] = ((n-1)*(m-1)) - total
        return res
         

