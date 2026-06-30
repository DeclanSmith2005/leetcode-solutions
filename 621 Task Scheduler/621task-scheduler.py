class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        res = 0
        heap = []
        for t in tasks:
            counts[t] += 1
        for letter, count in counts.items():
            heapq.heappush(heap, (-count, letter))
        q= deque([])
        reals = 0 
        for i in range(min(n+1, len(heap))):
            q.append(heapq.heappop(heap))
            reals+=1
        while len(q) < n+1:
            q.append((0,0))
        while True:
            if q[0][1] != 0:
                reals-=1
            if q[0][0] < -1:
                count, task = q.popleft()
                heapq.heappush(heap, (count+1, task))
            else:
                q.popleft()
            if heap:
                q.append(heapq.heappop(heap))
                reals+=1
            else:
                q.append((0,0))
            res +=1 
            if reals == 0 and len(heap) == 0:
                return res

        
        
            
