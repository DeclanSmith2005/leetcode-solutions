class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefixes = [0] * (n+1)
        res = []
        for start, end, num in bookings:
            if start< len(prefixes):
                prefixes[start] += num
            if end +1 < len(prefixes):
                prefixes[end+1] -= num
        for i in range(1, len(prefixes)):
            prefixes[i] += prefixes[i-1]
            res.append(prefixes[i])
        return res