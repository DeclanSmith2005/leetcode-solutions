class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robbing(start):
            lead, lag = 0 , 0
            for i in range(start, len(nums) + start -1 ):
                temp = max(lead, lag + nums[i%len(nums)])
                lag = lead
                lead = temp
            
            return lead
        return max(robbing(0), robbing(1))