class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        if len(nums)==1:
            return 0
        while left <= right:
            mid =  (left + right) //2
            if mid -1 < 0:
                if nums[mid+1] > nums[mid]:
                    left = mid+1
                    continue
                else:
                    return mid
            if mid +1 >= len(nums):
                if nums[mid-1] > nums[mid]:
                    right = mid-1
                    continue
                else:
                    return mid
            if nums[mid-1] < nums[mid]:
                if nums[mid+1] < nums[mid]:
                    return mid
                if nums[mid+1] > nums[mid]:
                    left = mid +1
                    continue
            right = mid-1
            
        return mid