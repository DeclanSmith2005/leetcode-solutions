class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0 
        res = 0
        unique = 0
        counts = defaultdict(int)
        for r in range(len(s)):
            counts[s[r]] += 1
            if counts[s[r]] == 1:
                unique += 1
            while unique > k:
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    unique -= 1
                l+=1
            res = max(res, r-l+1)
        return res 
                
                