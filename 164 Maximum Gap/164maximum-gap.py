class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maximum = float('-inf')
        minimum = float('inf')
        for i in nums:
            maximum = max(maximum, i)
            minimum = min(minimum, i)
        if maximum == minimum:
            return 0
        buckets = [[] for i in range(len(nums))]
        for i in range(len(nums)):
            fraction = ((nums[i] - minimum) / (maximum-minimum))* len(nums)
            if fraction == len(nums):
                fraction -=1
            buckets[floor(fraction)].append(nums[i])
        res = (maximum-minimum) / len(nums)
        curr = minimum
        for i in range(len(buckets)):
            if not buckets[i]:
                continue
            res = max(res, min(buckets[i]) - curr)
            curr = max(buckets[i])
        return res
            
            
