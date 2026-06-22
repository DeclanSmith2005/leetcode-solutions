class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # longest run of a set of 2 numbers
        counts = {}
        l  = 0
        res  = 0
        for r in range(len(fruits)):
            if fruits[r] not in counts:
                counts[fruits[r]] = 0
            while len(counts ) > 2:
                counts[fruits[l]] -= 1
                if counts[fruits[l]] == 0:
                    del counts[fruits[l]]
                l += 1
            counts[fruits[r]] += 1
            tmp = res
            res = max(res, r - l + 1)
        return res