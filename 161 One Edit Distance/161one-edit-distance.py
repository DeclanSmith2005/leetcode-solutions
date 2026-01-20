class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            tmp = s
            s = t
            t = tmp
        if s == t:
            return False
        if len(s) != len(t) and abs(len(s) - len(t)) != 1:
            return False
        i = 0
        while i < min(len(s), len(t)) and s[i] == t[i]:
            i+= 1
        return s[:i] + t[i] + s[i:] == t or s[:i] + s[i+1:] == t or s[:i] + t[i] + s[i+1:] == t