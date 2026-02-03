class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map2 = defaultdict(list)
        for i in range(len(nums2)):
            map2[nums2[i]].append(i)
        res = []
        for c in nums1:
            res.append(map2[c].pop())
        return res

