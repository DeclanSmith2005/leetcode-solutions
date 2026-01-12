class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        curr, total = [], 0
        candidates = sorted(candidates)

        def bt(ind):
            nonlocal curr, total
            if total == target:
                if total == target:
                    res.add(tuple(curr))
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] <= target:
                    total += candidates[i]
                    curr.append(candidates[i])
                    bt(i+1)
                    curr.pop()
                    total -= candidates[i]
                
                
        bt(0)
        return [list (i) for i in res]
