class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0 
        counts = defaultdict(int)
        for r, c in enumerate(s):
            counts[c] += 1
            while counts[c] > 1:
                counts[s[l]] -=1
                l += 1
            res = max(res, r - l + 1)
        return res