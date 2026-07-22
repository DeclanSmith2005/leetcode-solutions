class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = [0]*  (10**6 + 2)
        res = []
        for n in nums:
            freq[n] += 1
        for n in nums:
            if freq[n] == 1 and freq[n-1] == 0 and freq[n+1] == 0:
                res.append(n)
        
        return res