class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = {}  # city -> [roads into city, roads out of city]
        oriented = set()
        for cityA, cityB in connections:
            roads.setdefault(cityA, [[], []]) [1].append(cityB)
            roads.setdefault(cityB, [[],[]])  [0].append(cityA)
            
        q  = deque([0])
        reroutes = 0
        oriented.add(0)
        while q:
            curr = q.pop()
            for i in roads[curr][0]:
                if i not in oriented:
                    oriented.add(i)
                    q.appendleft(i)
            for i in roads[curr][1]:
                if i not in oriented:
                    oriented.add(i)
                    q.appendleft(i)
                    reroutes +=1
        return reroutes