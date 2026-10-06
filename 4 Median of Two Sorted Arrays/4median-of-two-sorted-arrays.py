class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if not nums2:
            nums2 = nums1
        elif nums2 and nums1 and nums1[-1] > nums2[-1]:
            tmp = nums2
            nums2 = nums1
            nums1 = tmp

        new = []
        l, r = 0, 0
        while r < len(nums2):
            if l < len(nums1) and nums1[l] <= nums2[r]:
                new.append(nums1[l])
                l +=1
            else:
                new.append(nums2[r])
                r+=1
        if len(new) % 2 == 0:
            return (new[len(new)//2]  + new[len(new)//2 - 1])/2
        else:
            return new[len(new)//2]