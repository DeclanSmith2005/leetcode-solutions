class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # try different start points for the subarray w/ binary search return when we find the minimal guy
        l , r  = 0, len(arr)-k
        while l < r:
            m = (l+r)//2
            if x - arr[m] > arr[m+k] -x :
                l = m + 1
            else:
                r = m
        return arr[l:l+k]
