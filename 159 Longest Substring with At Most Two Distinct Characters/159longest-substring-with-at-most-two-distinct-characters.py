class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        print('yo')
        chars = defaultdict(int)
        count = 0
        l = 0
        res = 0
        for r in range(len(s)):
            chars[s[r]] += 1
            if chars[s[r]] == 1:
                count += 1
            while count > 2:
                chars[s[l]] -=1
                if chars[s[l]] == 0:
                    count -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
