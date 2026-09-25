class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> list[str]:
        res = []
        for i in range(len(currentState)-1):
            a, b = currentState[i], currentState[i+1]
            if a + b == '++':
                res.append(currentState[:i] + '--' + currentState[i+2:])
        return res
                