class Solution:
    def minimumPushes(self, word: str) -> int:
        ppk = 1
        res= 0
        for i in range( len(word)):
            if i != 0 and i % 8 == 0:
                ppk += 1
            res += ppk
        return res