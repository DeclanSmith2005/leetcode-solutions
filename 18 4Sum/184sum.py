class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort, for stationary in nums, if too big, right goes down, if too small, left goes up, try to find an answer
        nums = sorted(nums)
        def ksum(tgt, nums, k):
            res = []
            if not nums:
                return res
            if k == 2:
                return twoSum(nums, tgt)
            
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in ksum(tgt - nums[i], nums[i+1:], k-1):
                        res.append([nums[i]] + subset)

            return res
        
        def twoSum(nums, tgt):
            res = []
            l, r = 0, len(nums)-1

            while l < r:
                total = nums[l] + nums[r]
                if total < tgt or l > 0 and nums[l] == nums[l-1]:
                    l +=1 
                elif total > tgt or (r < len(nums)-1 and nums[r] == nums[r+1]):
                    r-=1
                else:
                    res.append([nums[l], nums[r]])
                    l+=1
                    r-=1
            return res
        return ksum(target, nums, 4)
                