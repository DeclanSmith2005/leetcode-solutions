class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff  = arr[1]-arr[0] if abs(arr[2]-arr[1]) > abs(arr[1] - arr[0]) else arr[2] - arr[1]
        if diff == 0:
            return arr[0] 
        base = arr[0]
        l, r, m= 0, len(arr), 0
        while l < r:
            m = (l +r ) // 2
            if arr[m] == base + diff * m:
                l = m + 1
            else:
                r = m
        return arr[r] - diff
        
        








        