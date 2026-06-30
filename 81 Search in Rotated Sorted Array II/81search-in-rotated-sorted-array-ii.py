class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def bins(l , r):
            while l <= r: 
                m = (l + r) // 2
                if nums[m] == target:
                    return True
                elif nums[m] < target:
                    l = m+ 1
                else:
                    r = m - 1
            return False
                
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return bins(0, i-1) or bins(i, len(nums)-1)
        return bins(0, len(nums)-1)
