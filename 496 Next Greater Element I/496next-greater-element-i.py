class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # map nums[j] -> j
        res = []
        mapping = defaultdict(int)
        for i in range(len(nums2)):
            mapping[nums2[i]] = i
        for i in range(len(nums1)):
            j = mapping[nums1[i]]
            while j < len(nums2) and nums2[j] <= nums2[mapping[nums1[i]]]:
                j+= 1
            res.append(nums2[j] if j < len(nums2) else -1) 
        return res