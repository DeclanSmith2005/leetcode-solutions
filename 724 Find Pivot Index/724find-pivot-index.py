class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = [0]*len(nums)
        sumRight =[0]*len(nums)
        sumLeft[0] = nums[0]
        sumRight[-1] = nums[-1]
        for i in range(1, len(nums)):
            sumLeft[i] = sumLeft[i-1] + nums[i]
        for i in range(len(nums)-2, -1, -1):
            sumRight[i] = sumRight[i+1] + nums[i]
        for i in range(len(nums)):
            if sumRight[i] == sumLeft[i]:
                return i
        return -1