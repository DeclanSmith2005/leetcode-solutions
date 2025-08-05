class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        retList = []
        minHeap = [(nums1[0]+nums2[0], (0, 0))]
        added = set()
        while len(retList)<k:
            sumCurr, nums = heapq.heappop(minHeap)
            retList.append([nums1[nums[0]], nums2[nums[1]]])
            added.add(nums)
            if nums[0] < len(nums1)-1 and (nums[0]+1, nums[1]) not in added:
                heapq.heappush(minHeap, (nums1[nums[0]+1]+ nums2[nums[1]], (nums[0]+1, nums[1])))
                added.add((nums[0]+1, nums[1]))
            if nums[1] < len(nums2)-1 and (nums[0], nums[1]+1) not in added:
                heapq.heappush(minHeap, (nums1[nums[0]]+ nums2[nums[1]+1], (nums[0], nums[1]+1)))
                added.add((nums[0], nums[1]+1))
        return retList

        