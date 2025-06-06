class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        myMap = {}
        trueMap = {}
        for i in range(len(s)):
            if t[i] not in trueMap:
                trueMap[t[i]] = s[i]
            else:
                if trueMap[t[i]] != s[i]:
                    return False
                    
            if s[i] not in myMap:
                myMap[s[i]] = t[i]
            else:
                if myMap[s[i]] != t[i]:
                    return False
            
        return True
            