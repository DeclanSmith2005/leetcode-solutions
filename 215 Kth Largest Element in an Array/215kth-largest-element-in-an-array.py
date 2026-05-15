class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        for i in range(len(nums)):
            counts[nums[i]] += 1
        for i in range(max(nums), min(nums)-1, -1):
            k -= counts[i]
            if k <= 0:
                return i 
        return nums[len(nums)-k]
                   




