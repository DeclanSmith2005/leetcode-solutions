class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def canComplete(check):
            trips = 0
            for t in time:
                trips += check // t
            return trips >= totalTrips

        l, r = 0 , (totalTrips * min(time)) 
        while l < r:
            m = (l + r) // 2
            if canComplete(m):
                r = m
            else:
                l = m + 1
        return r

       