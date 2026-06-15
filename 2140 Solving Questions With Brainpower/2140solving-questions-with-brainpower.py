class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def dp(ind):
            if ind in memo:
                return memo[ind]
            if ind >= len(questions):
                return 0
            score, cost = questions[ind]
            memo[ind] = max(dp(ind+1), dp(ind+cost+1) + score)
            return memo[ind]
        return dp(0)
