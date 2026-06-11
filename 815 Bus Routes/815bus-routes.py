class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source:
            return 0

        lineStops = defaultdict(set) # line -> List[stops]
        stopConnections = defaultdict(set) # stop - > list[lines]
        lineConnections = defaultdict(set) # line - > list[lines]
        # write a dp guy that checks if destination is on current line, if not explore all neighboring lines, storing lowest dist and pruning where necessary

        for line in range(len(routes)):
            for stop in range(len(routes[line])):
                lineStops[line].add(routes[line][stop])
                stopConnections[routes[line][stop]].add(line)

        for line in range(len(routes)):
            for stop in lineStops[line]:
                lineConnections[line] |= stopConnections[stop]
            if line in lineConnections[line]:
                lineConnections[line].remove(line)

        q = deque(list(stopConnections[source]))
        seen = set()
        switches= 1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                seen.add(curr)
                if target in lineStops[curr]:
                    return switches
                for l in lineConnections[curr]:
                    if l not in seen:
                        q.append(l)
            switches += 1 
        return -1
