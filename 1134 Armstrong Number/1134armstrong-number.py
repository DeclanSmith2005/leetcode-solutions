class Solution:
    def isArmstrong(self, n: int) -> bool:
        num = str(n)
        k = len(num)
        total = 0
        for c in num:
            total += int(c)**k
        return total == n
            
