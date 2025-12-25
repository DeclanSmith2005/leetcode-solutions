class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        picks = sorted(range(len(nums2)), key= lambda i: -nums2[i])
        heap = []
        total = 0 
        for i in range(k):
            heapq.heappush(heap, nums1[picks[i]])
            total += nums1[picks[i]]
        ans = total * nums2[picks[k-1]]
        for i in range(k , len(nums2)):
            if heap[0] < nums1[picks[i]]:
                total -= heapq.heappop(heap)
                heapq.heappush(heap, nums1[picks[i]])
                total += nums1[picks[i]]
                ans = max(ans, total * nums2[picks[i]]) 
        return ans


            