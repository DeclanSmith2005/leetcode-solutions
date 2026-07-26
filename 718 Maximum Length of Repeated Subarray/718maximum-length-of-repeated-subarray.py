class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for i in range(len(nums1))] for k in range(len(nums2))]
            
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[j][i] =  dp[j-1][i-1] + 1 if i > 0 and j > 0 else 1
        return max(max(row) for row in dp)