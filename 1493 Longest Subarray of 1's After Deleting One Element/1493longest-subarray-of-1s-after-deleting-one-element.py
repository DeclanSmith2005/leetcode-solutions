class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev, curr, res, i = 0, 0 ,0, 0
        noZero = True
        while i < len(nums):
            while i < len(nums) and nums[i] == 1:
                curr+=1
                i+=1
            if  i < len(nums) and nums[i] == 0:
                noZero = False
            res = max(res, prev + curr)
            prev, curr = curr, 0
            if i < len(nums)-1 and nums[i+1] == 0:
                prev = 0 
            i+=1
        return res-1 if noZero else res

            
            
            
            

        
            

        