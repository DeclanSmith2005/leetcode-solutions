class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) <= len(nums2):
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
        k = m + n -1
        n, m = n-1, m-1
        while  m > -1 and n > -1:
            if nums1[m] > nums2[n]:
                nums1[k] = nums1[m]
                m-= 1
            else:
                nums1[k] = nums2[n]
                n-= 1
            k-=1
        if m == -1:
            while n > -1:
                nums1[n] = nums2[n]
                n-=1
        

