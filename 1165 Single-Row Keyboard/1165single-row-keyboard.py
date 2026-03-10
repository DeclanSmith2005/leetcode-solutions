class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = {}
        for k in range(len(keyboard)):
            pos[keyboard[k]] = k
        res = pos[word[0]]
        for i in range(len(word)-1):
            res += abs(pos[word[i]] - pos[word[i+1]])
        return res
        