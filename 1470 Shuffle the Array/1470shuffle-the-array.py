class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        l, r = 0 , n
        while r < len(nums):
            res.extend([nums[l], nums[r]])
            l+=1 ; r +=1 
        return res