class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dq = deque([])
        rq = deque([])
        for i,s in enumerate(senate):
            if s == 'R':
                rq.append(i)
            else:
                dq.append(i)
        while rq and dq:
            r = rq.popleft()
            d = dq.popleft()

            if d < r:
                dq.append(d + len(senate))
            else:
                rq.append(r + len(senate))

        return "Radiant" if rq else "Dire"