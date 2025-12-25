class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        total=0
        for i in range(32):
            if c & 1 == 1:
                if not (1 & (a|b)):
                    total +=1
            else:
                if 1 & (a & b):
                    total +=2
                elif 1&(a|b):
                    total += 1
            a, b, c = a>>1, b>>1, c>>1
        return total