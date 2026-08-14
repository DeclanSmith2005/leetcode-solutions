class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counts = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            while counts[s[r]] > 2:
                counts[s[l]] -=1
                l +=1
            res = max(res, r-l + 1)
        return res
            