class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        retList = []
        existing = set()
        def backTrack(total, curr, l):
            if total == target:               
                retList.append(curr[:])
                return 
            
            for i in range(l, len(candidates)):
                num = candidates[i]
                if total + num <= target:
                    curr.append(num)
                    total += num
                    backTrack(total, curr, i)
                    total-= num
                    curr.pop()
        backTrack(0, [], 0)
        return retList