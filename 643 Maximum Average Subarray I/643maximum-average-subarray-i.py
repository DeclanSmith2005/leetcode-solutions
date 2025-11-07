class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l , r = 0, k
        curr = maxAvg = sum(nums[:k])
        while r < len(nums):
            curr = curr + ( - nums[l] + nums[r])
            maxAvg = max(maxAvg, curr)
            r, l = r+1, l+1
        return maxAvg/k