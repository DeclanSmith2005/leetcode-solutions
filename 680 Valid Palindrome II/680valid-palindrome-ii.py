class Solution:
    def validPalindrome(self, s: str) -> bool:
        def vp(string):
            l , r = 0, len(string)-1
            while l < r and string[l] == string[r]:
                l += 1; r-=1 
            return (l, r)
        l, r = vp(s)
        check1, check2 = "", ""
        if l >= r:
            return True
        check1 = s[:l] + s[l+1:]
        check2 = s[:r] + s[r+1:]
        a, b = vp(check1)
        c, d = vp(check2)
        return a >= b or c >= d