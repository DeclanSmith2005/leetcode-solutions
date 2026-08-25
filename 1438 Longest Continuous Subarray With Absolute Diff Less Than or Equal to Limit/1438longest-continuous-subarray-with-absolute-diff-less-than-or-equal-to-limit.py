class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0 
        res = 0
        counts = defaultdict(int)
        mini, maxi = [],[]
        for r in range(len(nums)):
            heapq.heappush(mini, (nums[r], r))
            heapq.heappush(maxi, (-nums[r], r))
            while -maxi[0][0] - mini[0][0] > limit:
                l += 1
                while mini and mini[0][1] < l:
                    heapq.heappop(mini)
                while maxi and maxi[0][1] < l:
                    heapq.heappop(maxi)
            res = max(res, r-l+1)
        return res
        
        