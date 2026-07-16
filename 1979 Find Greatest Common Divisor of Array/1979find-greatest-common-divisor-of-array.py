class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini, maxi = min(nums), max(nums)
        while mini:
            tmp = maxi % mini
            maxi = mini
            mini = tmp
        return maxi