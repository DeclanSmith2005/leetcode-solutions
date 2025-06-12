class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        insertInd = 0
        left, right = 0, n - 1
        while (left <= right):
            mid = (right + left)//2
            if intervals[mid][0] == newInterval[0]:
                insertInd = mid
                break
            elif intervals[mid][0] < newInterval[0]:
                if mid == n-1 or intervals[mid+1][0] >= newInterval[0]:
                    insertInd = mid
                    break
                left  = mid + 1
            else:
                if mid == 0:
                    insertInd = -1
                    break
                if intervals[mid-1][0] <= newInterval[0]:
                    insertInd = mid-1
                    break
                right  = mid - 1
        retList  = []
        i = 0
        while i < insertInd+1 and i < n:
            retList.append(intervals[i])
            i+=1
        retList.append(newInterval)
        while i < n:
            retList.append(intervals[i])
            i+=1
        intervals = retList
        n+=1
        retList = []
        i = 0
        while i < n:
            outerBounds = intervals[i]
            i+=1
            while ( i < n and outerBounds[1]>= intervals[i][0]):
                outerBounds[0] = min(outerBounds[0], intervals[i][0])
                outerBounds[1] = max(outerBounds[1], intervals[i][1])
                i+=1
            retList.append(outerBounds)
        return retList
