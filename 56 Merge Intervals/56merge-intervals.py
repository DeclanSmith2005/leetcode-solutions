class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals, iterate through the list
        # if the start is before or equal to the end of the highest, interval, end = max(their ends)
        # otherwise append the interval
        res= [1, 3]
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if res[-1][1] >= s:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append(intervals[i])
        return res