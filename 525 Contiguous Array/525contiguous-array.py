class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        left= {0:-1}
        curr = 0
        res = 0
        for i in range( len(nums)):
            curr += -1 if nums[i] == 0 else 1
            if curr not in left:
                left[curr] = i
            else:
                res = max(res, i - left[curr] )
       # print(left)
        return res



        

