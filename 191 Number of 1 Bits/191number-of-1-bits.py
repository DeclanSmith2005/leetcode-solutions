class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n) [2:]
        total = 0 
        for i in n:
            if i == "1":
                total +=1
        return total