class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        delete = set()
        for i in range(len(intervals)):
            if i in delete:
                continue
            s, e = intervals[i]
            while i < len(intervals) - 1 and intervals[i+1][0] >= s and intervals[i+1][1] <= e:
                i+=1
                delete.add(i)
        return len(intervals) - len(delete) 