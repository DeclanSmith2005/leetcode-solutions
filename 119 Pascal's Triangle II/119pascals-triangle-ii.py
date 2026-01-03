class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0 or rowIndex == 1:
            return [1] if rowIndex == 0 else [1,1]
        curr = [1, 1]
        for i in range(2, rowIndex+1):
            nxt = [1]
            for k in range(1,len(curr)):
                nxt.append(curr[k-1] + curr[k])
            curr = nxt[:] + [1]
        return curr