class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        complements = {}
        removals  = 0
        def rem(val):
            if complements[val] > 1:
                complements[val]-=1
            else:
                del complements[val]
        for i in range(len(nums)):
            complements[nums[i]] = complements.get(nums[i], 0) + 1
        for i in range(len(nums)):
            comp = k - nums[i]
            if comp in complements:
                if nums[i] == comp and complements[comp] < 2 or nums[i] not in complements:
                    continue
                removals += 1
                rem(nums[i])
                rem(comp)
        return removals
                

