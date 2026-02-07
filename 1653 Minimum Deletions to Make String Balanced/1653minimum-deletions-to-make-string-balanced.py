class Solution:
    def minimumDeletions(self, s: str) -> int:
        aBefore = [0 for i in range(len(s))]
        bAfter = [0 for i in range(len(s))]
        numAs = 0 
        numBs = 0
        for i in range(len(s)-1, -1, -1):
            aBefore[i] = numAs
            if s[i] == 'a':
                numAs +=1
        for i in range(len(s)):
            bAfter[i] = numBs
            if s[i] == 'b':
                numBs += 1
        res = len(s)
        for i in range(len(s)):
            res = min(res, aBefore[i]+ bAfter[i])
        return res
