class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold = [0]* len(s)
        for word in words:
            for l in range(len(s) - len(word)+1):
                if s[l: l+len(word)] == word:
                    for i in range(l, l+len(word)):
                        bold[i] = 1
        res = []
        for i in range(len(s)):
            if bold[i] == 1 and (i== 0 or bold[i-1] == 0):
                res.append('<b>')
            res.append(s[i])
            if bold[i] == 1 and (i == len(s)-1 or bold[i+1] == 0):
                res.append('</b>')
        return "".join(res)
