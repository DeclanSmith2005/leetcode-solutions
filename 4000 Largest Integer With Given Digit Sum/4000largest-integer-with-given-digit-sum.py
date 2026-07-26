class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        for i in range((10**n)-1, -1, -1):
            if sum(int(d) for d in str(i)) == s:
                return i
        return -1
            