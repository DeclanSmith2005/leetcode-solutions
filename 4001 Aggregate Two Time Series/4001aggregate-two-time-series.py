class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        a = deque(series1)
        b = deque(series2)
        res= []
        
        while a or b:
            if not a:
                a = b
                b = None
            if b and a[0][0] > b[0][0]:
                tmp = a
                a = b
                b = tmp
            res.append([a[0][0], a[0][1]+ b[0][1] if b else a[0][1]])
            if b and a[0][0] == b[0][0]:
                b.popleft()
            a.popleft()
        return res
            
            