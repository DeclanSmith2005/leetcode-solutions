class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:       
        graph = {}
        if n != len(edges) +1 :
            return False
        if len(edges) == 0:
            return True
        for a, b in edges:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]
            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]
        
        q = deque([(edges[0][0], None)])
        seen = set()
        while q:
            curr, prev = q.pop()
            if curr in seen:
                return False
            for i in graph[curr]:
                if i != prev:
                    q.appendleft((i,curr))
            seen.add(curr)

       
        return True if len(seen) == len(edges) +1 else False
            
