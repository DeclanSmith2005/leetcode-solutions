class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myMap = {}
        left = 0
        for i in range(len(nums)):
            if i > k:
                if nums[left] in myMap and myMap[nums[left]] == left:
                    del myMap[nums[left]]
                left+=1
            if nums[i] in myMap:
                return True
            else:
                myMap[nums[i]] = i
            
        return False
            