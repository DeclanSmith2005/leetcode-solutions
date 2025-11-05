class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 
        k = 0
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        while i < len(t):
            if t[i] == s[k]:
                k+=1
            if k == len(s):
                return True
            i+=1
        return False