class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        minDif = float('inf')
        check = SortedList([])
        for i in range(x, len(nums)):
            check.add(nums[i-x])
            left = 0
            right = len(check)
            while left < right:
                mid = (right + left )//2
                if nums[i] >  check[mid]:
                    left = mid + 1
                else:
                    right = mid
            if left < len(check):
                minDif = min(minDif, abs(nums[i] - check[left]))
            if left - 1 >= 0:
                minDif = min(minDif, abs(nums[i] - check[left-1]))                
        return minDif



