class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        #sqare size, starting row, starting col
        res = 0
        def checkSS(size):
            nonlocal res
            for sr in range(len(mat)-size+1):
                total = 0 
                for sc in range(len(mat[0])-size+1):
                    if sc == 0:
                        for r in range(sr, sr+ size):
                            for c in range(sc, sc + size):
                                total += mat[r][c]
                    else:
                        for r in range(sr, sr + size):
                            total -= mat[r][sc-1]
                        for r in range(sr, sr+ size):
                            total += mat[r][sc + size -1]
                    if total <= threshold:
                        res = size
                        return True
            return False
        l ,r = 0, min(len(mat), len(mat[0]))+1
        while l <= r:
            m = (l + r)//2
            if checkSS(m):
                l = m + 1
            else:
                r = m - 1
        return res