class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = res = 0
        maxFreq = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            maxFreq = max(maxFreq, counts[s[r]])
            if (r+1 - l) - maxFreq <= k:
                res = max(res, r+1 - l)
            else:
                counts[s[l]]-=1
                l+=1
        return res
