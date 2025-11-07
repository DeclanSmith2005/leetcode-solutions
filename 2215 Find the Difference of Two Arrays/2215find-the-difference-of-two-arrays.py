class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ones, twos = set(nums1) ,  set(nums2)
        return [list(ones-twos),list(twos-ones)]
        