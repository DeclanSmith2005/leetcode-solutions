class Solution:
    def longestSubarray(self, nums):
        n = len(nums)
        if n == 1:
            return 1

        left = [1] * n
        right = [1] * n

        # left[i] = length of non-decreasing subarray ending at i
        for i in range(1, n):
            if nums[i - 1] <= nums[i]:
                left[i] = left[i - 1] + 1

        # right[i] = length of non-decreasing subarray starting at i
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                right[i] = right[i + 1] + 1

        ans = 1
        for j in range(n):
            if j == 0:
                ans = max(ans, right[j + 1] + 1)
            elif j == n - 1:
                ans = max(ans, left[j - 1] + 1)
            elif nums[j - 1] <= nums[j + 1]:
                ans = max(ans, left[j - 1] + right[j + 1] + 1)
            else:
                ans = max(ans, max(left[j - 1], right[j + 1]) + 1)

        return ans