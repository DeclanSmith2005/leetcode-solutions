class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        right  = 0
        total = 0
        n = len(nums)
        total += nums[0]
        least = n+1
        while (total < target and right < n-1):
            right += 1
            total += nums[right]
        if total < target: return 0
        least = min ( least, right-left+1)
        while ( least > 1 and left != right):
            if total >= target:
                left += 1
                total -= nums[left-1] 
            elif right+1 < n:
                right += 1
                total += nums[right]
            else:
                return least
            if total >= target:
                least = min ( least, right-left+1)
        if (left == right and nums[left] >= target):
            return 1
        return least
        
            
            