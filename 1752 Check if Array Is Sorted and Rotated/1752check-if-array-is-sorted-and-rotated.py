class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                nums = nums[i+1 : len(nums)] + nums[0:i+1]
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                return False
        return True