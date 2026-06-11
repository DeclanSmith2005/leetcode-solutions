class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # first determine the depth of the tree 
        # even weights have no effect on parity
        # therefore of all 2^depth posible assignments exactly half r gonna be odd, so 2^depth -1 
        # bfs build the tree to find max depth?? 
        adj = defaultdict(list)
        for a, b in edges:
            adj[b].append(a); adj[a].append(b)
        seen = set([1])
        q = deque([1])
        depth = -1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                seen.add(curr)
                for child in adj[curr]:
                    if child not in seen:
                        q.append(child)
            depth += 1
        return (2**(depth-1))%(10**9+7)

            
