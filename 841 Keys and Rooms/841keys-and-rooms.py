class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set([0])
        q = deque([0])
        while q:
            curr = q.popleft()
            for i in rooms[curr]:
                if i not in seen:
                    q.append(i)
                    seen.add(i)
        print(seen)
        return len(seen) == len(rooms)
        
            