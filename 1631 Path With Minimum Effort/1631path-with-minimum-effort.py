class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0,0,0)]
        dirs = [(0,1), (1, 0), (-1, 0), (0, -1)]
        best = defaultdict(lambda: float('inf'))
        best[(0,0)] = 0
        processed = set()
        
        while heap:
            cost, r, c = heapq.heappop(heap)
            if (r, c) in processed:
                continue
            processed.add((r, c))
            if (r, c) == (len(heights)-1, len(heights[0])-1):
                return cost
                
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr > len(heights)-1 or nc < 0 or nc > len(heights[0])-1 or (nr, nc) in processed:
                    continue
                newCost = max(cost, abs(heights[nr][nc] - heights[r][c]))

                if newCost < best[(nr, nc)]:
                    best[(nr, nc)] = newCost
                    heapq.heappush(heap, (newCost, nr, nc))
        return -1