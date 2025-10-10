class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = set()
        def recurse(i):
            if i in memo:
                return False
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    if i +len(word) == len(s):
                        return True
                    if recurse(i+len(word)):
                        return True
            memo.add(i)
            return False
        
        return recurse(0)

            
                    
