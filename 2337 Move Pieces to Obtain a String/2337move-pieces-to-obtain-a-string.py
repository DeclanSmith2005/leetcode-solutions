class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start  = [ (start[l],  l) for l in range(len(start))  if start[l]   != "_"]
        target = [ (target[l], l) for l in range(len(target)) if target[l]  != "_"]
        if len(start) != len(target):
            return False
        for i in range(len(start)):
            if start[i][0] != target[i][0]:
                return False
            if start[i][0] == 'R' and start[i][1] > target[i][1]:
                return False
            elif start[i][0] == 'L' and start[i][1] < target[i][1]:
                return False
        return True
            