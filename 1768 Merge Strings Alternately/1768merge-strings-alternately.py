class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        k = 0
        while i< len(word1) and k < len(word2):
            res.append(word1[i])
            i+=1
            res.append(word2[k])
            k+=1
        if i == len(word1):
            res.append(word2[k:])
        else:
            res.append(word1[i:])
        return "".join(res)
        
