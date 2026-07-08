class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)]
        counts = defaultdict(int)
        res = []
        for num in nums:
            counts[num] += 1
        for num, count in counts.items():
            buckets[count].append(num)
        for i in range((len(nums)//3)+1, len(nums)+1):
            res.extend(buckets[i])
        return res