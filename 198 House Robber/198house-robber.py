class Solution:
    def rob(self, nums: List[int]) -> int:
        lead, lag = 0, 0
        for num in nums:
            new = max(lag + num, lead)
            lag = lead
            lead = new
        return max(lag, lead)