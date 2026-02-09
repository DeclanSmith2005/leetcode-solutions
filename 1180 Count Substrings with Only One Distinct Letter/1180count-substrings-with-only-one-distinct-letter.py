class Solution:
    def countLetters(self, s: str) -> int:
        ans = 0
        l = 0
        res = 0
        for r in range(1, len(s)+1):
            if r == len(s) or s[r] != s[l]:
                res += ((r-l)*((r-l)+1)) / 2
                l = r
        return int(res)