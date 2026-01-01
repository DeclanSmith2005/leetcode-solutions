class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1 or numRows == 2:
            return [[1]] if numRows == 1 else [[1], [1,1]]
        res = [[1], [1,1]]
        curr = [1, 1]
        for i in range(2, numRows):
            nxt = [1]
            for k in range(1,len(curr)):
                nxt.append(curr[k-1] + curr[k])
            res.append(nxt[:] + [1])
            curr = nxt[:] + [1]
        return res