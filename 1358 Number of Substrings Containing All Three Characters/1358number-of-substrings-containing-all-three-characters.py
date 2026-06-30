class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while all(i > 0 for i in count.values()):
                res += len(s) - r
                count[s[l]] -= 1
                l += 1
        return res
