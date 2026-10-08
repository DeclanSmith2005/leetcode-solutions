class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = ((l +r) // 2) + 1
            if m < len(nums)-1 and nums[m] > nums[0]:
                l = m
            else:
                r = m - 1
        offset = l

        def find(l, r):
            while l <= r:
                m = (l + r)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m + 1
            return -1
        
        if nums[0] <= target <= nums[offset]:
            return find(0, offset)

        return find(offset + 1, len(nums) - 1)

      