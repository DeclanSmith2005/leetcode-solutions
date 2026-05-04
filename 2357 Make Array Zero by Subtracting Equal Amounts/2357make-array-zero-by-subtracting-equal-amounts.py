class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        nextArr = []
        for i in nums:
            if i > 0:
                nextArr.append(i)
        nums = nextArr
        ops = 0 
        while len(nums) > 0:
            nextArr = []
            for i in nums:
                if i - nums[0] > 0:
                    nextArr.append(i - nums[0])
            nums= nextArr
            ops += 1
        return ops