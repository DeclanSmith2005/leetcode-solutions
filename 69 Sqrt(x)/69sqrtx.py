class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0 
        right = x 
        while True:
            mid = (left + right)//2
            if (mid+1)**2 > x and mid**2 <= x:
                return mid
            if mid**2 > x:
                right = mid-1
            else:
                left = mid +1

    