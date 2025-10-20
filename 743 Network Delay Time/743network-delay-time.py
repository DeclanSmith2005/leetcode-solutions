class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neighbors = {}
        edges = {}
        traversalTime = [float("inf") for i in range(n)]
        if k < len(traversalTime)+1:
            traversalTime[k-1] = 0
        else:
            return -1
        # longestTime = float("-inf")
        for i in times:
            edges[(i[0],i[1])] = i[2]
            if i[0] in neighbors:
                neighbors[i[0]].append(i[1])
            else:
                neighbors[i[0]] = [i[1]]

        def recurse(time, node):
            nonlocal check
            if node in check:
                check.remove(node)
            if node not in neighbors:
                return
            nodes = neighbors[node]
            for n in nodes:
                timeNext = time + edges[(node, n)] 
                if timeNext < traversalTime[n-1]:
                    traversalTime[n-1] = timeNext
                    recurse(timeNext, n)

        check = set([i for i in range(1, n+1)])
        # for i in range(1, n+1):
        #     check.add(i)
        recurse(0, k)
        # maximum = float('-inf')
        # for i in traversalTime:
        #     maximum = max(i, maximum)
        return max(traversalTime) if len(check) == 0 else -1
