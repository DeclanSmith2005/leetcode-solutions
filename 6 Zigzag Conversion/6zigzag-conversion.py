class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[""]* len(s) for _ in range(numRows)]
        r, c, i = 0 , 0, 0
        while i < len(s):
            while r < numRows and i < len(s):
                res[r][c] = s[i]
                i, r = i +1, r +1
            r = max(r-2, 0); c+=1
            while r > 0 and c < len(s) and i < len(s):
                res[r][c] = s[i]
                i, r, c = i + 1, r-1, c+1
        return "".join("".join(row) for row in res)

            