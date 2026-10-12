class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        base = 0 
        while 3**base < n: 
            base += 1
        return 3**base == n