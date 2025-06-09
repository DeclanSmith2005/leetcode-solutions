class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordMap = {}
        letterMap = {}
        s = s.split(" ")

        if len(s) != len(pattern):
            return False

        for i in range(len(s)):
            if s[i] not in wordMap:
                wordMap[s[i]] = pattern[i]
            elif wordMap[s[i]] != pattern[i]:
                return False

            if pattern[i] not in letterMap:
                letterMap[pattern[i]] = s[i]
            elif letterMap[pattern[i]] != s[i]:
                return False
        
        return True
                
                