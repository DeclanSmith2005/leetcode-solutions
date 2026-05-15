class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        remRows = [len(mat[0])] * len(mat)
        remCols = [len(mat)] * len(mat[0])

        windowVals = {}
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                windowVals[mat[r][c]] = (r, c)
        
        for i in range(len(arr)):
            r, c = windowVals[arr[i]]
            remCols[c] -=1
            remRows[r] -=1
            if remCols[c] == 0 or remRows[r] == 0:
                return i
        
        return len(arr)-1