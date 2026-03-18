class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        # first merge all intervals that are in there
        res = []
        remStart, remEnd = toBeRemoved
        for start, end in intervals:
            if start <= remStart < end or start <= remEnd < end:
                res.append([start, remStart]) if start < remStart else None
                res.append([remEnd, end]) if remEnd < end else None
            else:
                if end < remStart or start > remEnd:
                    res.append([start, end]) 
        return res
                
