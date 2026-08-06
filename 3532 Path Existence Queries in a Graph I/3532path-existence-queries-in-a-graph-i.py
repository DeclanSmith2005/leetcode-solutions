class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        res = []
        parents = [i for i in range(len(nums))]
        rank = [1 for i in range(len(nums))]

        def find(n):
            while parents[n] != n:
                n = parents[n]
            return n
        
        def union(a, b):
            p1, p2 = find(a), find(b)
            if rank[p1] > rank[p2]:
                parents[p2] = p1
            else:
                parents[p1] = p2

        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i-1]) <= maxDiff:
                union(i, i-1)
        
        for a, b in queries:
            res.append(parents[a] == parents[b])
        
        return res


        




