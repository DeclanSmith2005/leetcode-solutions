class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        res = []
        buckets = [[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            counts[nums[i]] += 1
        for val, count in counts.items():
            buckets[count].append(val)
        i = -1 
        while len(res) < k:
            res.extend(buckets[i])
            i-=1
        while len(res) > k:
            res.pop()
        return res