class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        minPrefix = defaultdict(lambda: float('inf'))
        res = float('-inf')
        prefix = 0
        for num in nums:
            curr_sum = prefix + num

            if num - k in minPrefix:
                res = max(res, curr_sum - minPrefix[num - k])

            if num + k in minPrefix:
                res = max(res, curr_sum - minPrefix[num + k])

            minPrefix[num] = min(minPrefix[num], prefix)

            prefix += num

        return res if res != float('-inf') else 0