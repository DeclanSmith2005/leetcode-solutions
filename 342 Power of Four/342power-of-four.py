class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num = 4
        prev = 1
        while num < n:
            prev = num
            num *= num
        if num == n:
            return True
        num = prev
        while (num < n):
            num *=4
        if num == n:
            return True
        else:
            return False
        
    
    