class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        myMap = {}
        for i in items:
            if i[0] not in myMap:
                myMap[i[0]] = []
            heapq.heappush(myMap[i[0]], -1*i[1])
        res = []
        for item in myMap.items():
            count = 5
            avg = []
            while item[1] and count > 0:
                avg.append((-1)*heapq.heappop(item[1]))
                count-=1
            res.append([item[0], sum(avg) // (5-count)])
        return sorted(res, key = lambda i: i[0])
            