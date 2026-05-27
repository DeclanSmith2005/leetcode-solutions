class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        dist = float('inf')
        res = 0
        for i in range(len(nums)):
            if i > 1 and i == i-1:
                continue
            l, r = i + 1, len(nums)-1
            while l < r:
                if nums[l] == nums [l-1] and nums[l] != nums[r] and nums[l] != nums[i]:
                    l+=1
                    continue
                if abs(nums[i] + nums[l] + nums[r] - target) < dist:
                    res = nums[i] + nums[l] + nums[r]
                    dist = min(dist, abs(nums[i] + nums[l] + nums[r] - target))
                if nums[i] + nums[l] + nums[r] == target:
                    return target
                elif nums[i] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res