class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(tp):
            tp = tp.split(":")
            return int(tp[0]) * 60 + int(tp[1])

        arr = []
        seen = set()
        for i in timePoints:
            curr = convert(i)
            if i in seen:
                return 0
            seen.add(i)
            arr.append(convert(i))

        arr = sorted(arr)
        curr = arr[0]
        res = float('inf')
        for i in range(1, len(arr)):
            res = min( res, arr[i] - curr )
            curr = arr[i]
        
        return min(res, 1440 - arr[-1] + arr[0])
        