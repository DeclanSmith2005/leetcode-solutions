class Solution:
    def longestPalindrome(self, s: str) -> str:
        res= ''
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l-1, r+1
            res = max(res, s[l+1:r], key= len)
            l, r = i-1, i
            while l >= 0 and r < len(s) and  s[l] == s[r]:
                l, r = l-1, r+1
            res = max(res, s[l+1:r], key = len)
        return res if len(s) > 1 else s

