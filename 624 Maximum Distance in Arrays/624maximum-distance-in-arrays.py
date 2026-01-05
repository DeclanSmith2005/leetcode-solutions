class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        for a in arrays:
            a.sort()

        mx1 = (-10**18, -1)   # (value, index)
        mx2 = (-10**18, -1)
        mn1 = (10**18, -1)
        mn2 = (10**18, -1)

        for i in range(len(arrays)):
            hi = arrays[i][-1]
            lo = arrays[i][0]

            # track top 2 maximum "hi"
            if hi > mx1[0]:
                mx2 = mx1
                mx1 = (hi, i)
            elif hi > mx2[0]:
                mx2 = (hi, i)

            # track top 2 minimum "lo"
            if lo < mn1[0]:
                mn2 = mn1
                mn1 = (lo, i)
            elif lo < mn2[0]:
                mn2 = (lo, i)

        return mx1[0] - mn1[0] if mx1[1] != mn1[1] else max(mx1[0] - mn2[0], mx2[0] - mn1[0])
