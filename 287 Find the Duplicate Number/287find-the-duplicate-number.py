class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def getCount(num):
            count = 0 
            for val in nums:
                if val <= num:
                    count +=1
            return count > num

        l, r = 0, len(nums)
        while l < r:
            m = (l+r)//2
            if getCount(m):
                r = m 
            else:
                l = m + 1
        return l