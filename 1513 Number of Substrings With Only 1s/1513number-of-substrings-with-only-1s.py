class Solution:
    def numSub(self, s: str) -> int:
        options = s.split("0")
        res = 0
        for n in options:
            n = len(n)
            res += (n+1) * n//2
        return res % (10**9 + 7)

