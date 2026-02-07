class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1
        while l < r:
            t = s[l]
            s[l] = s[r]
            s[r] = t
            l, r= l+1, r-1
        
        for i in range(len(s)):
            if s[i] == " " or (i != 0 and s[i-1] != " "):
                continue
            k = i
            while k < len(s) and s[k] != ' ':
                k+=1
            k-=1
            while i < len(s) and k >-1 and i < k:
                t = s[i]
                s[i] = s[k]
                s[k] = t
                i, k = i+1, k-1