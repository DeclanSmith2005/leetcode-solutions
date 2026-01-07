class Solution:
    def findPermutation(self, s: str) -> List[int]:
        l = 0
        res = []
        for r in range(1, len(s)+1):
            if s[r-1] == 'I':
                for i in range(r-1, l-1, -1):
                    res.append(i+1)
                l = r 
        for i in range(len(s), l-1, -1):
            res.append(i+1)
        return res


        