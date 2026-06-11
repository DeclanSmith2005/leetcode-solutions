class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, 1
        res = 0
        seen = set()
        while r < len(nums):
            if abs(nums[r] - nums[l]) > k:
                l += 1
            elif abs(nums[r] - nums[l]) < k:
                r +=1 
            else:
                if ((nums[l], nums[r])) not in seen and l != r:
                    res += 1
                    seen.add((nums[l],nums[r]))
                r+=1
        return res