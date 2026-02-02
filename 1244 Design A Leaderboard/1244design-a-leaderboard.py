class Leaderboard:

    def __init__(self):
        self.leaderboard = []

    def addScore(self, playerId: int, score: int) -> None:
        print(self.leaderboard)
        inside = False
        for i in self.leaderboard:
            if i[1] == playerId:
                i[0] -= score
                inside = True
        if not inside:
            self.leaderboard.append([-1*score, playerId])
        heapq.heapify(self.leaderboard) 

    def top(self, K: int) -> int:
        tmp = []
        for i in range(K):
            if not self.leaderboard:
                break
            tmp.append(heapq.heappop(self.leaderboard))
        for i in tmp:
            heapq.heappush(self.leaderboard, i)
        print(tmp)
        return sum(-1* i[0] for i in tmp)

    def reset(self, playerId: int) -> None:
        tmp = []
        while self.leaderboard and len(self.leaderboard[0]) > 0:
            val, pid = heapq.heappop(self.leaderboard)
            if pid != playerId:
                heapq.heappush(tmp, [val, pid])
        self.leaderboard = tmp


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)