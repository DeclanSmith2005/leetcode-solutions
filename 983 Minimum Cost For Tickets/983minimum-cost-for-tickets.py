class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #dp on number of days left / solvedd  w/ greedy optimization of only purchasing passes starting on days that I need to 
        # i think dp on days solved make more sense because that subproblem decends down into future subproblems via the covered array, whereas in bottom up buying new passes recovers guys we have alrady processed
        memo = {}
        covered = [1] * 366
        for day in days:
            covered[day] = 0

        def dp(startDay, covered):
            if startDay > 365:
                return 0
            if startDay in memo:
                return memo[startDay]
            if covered[startDay]:
                return dp(startDay+1, covered)
            
            best = float('inf')
            for duration, cost in zip((1, 7, 30), costs):
                best = min(best, cost + dp(startDay + duration, covered))
            memo[startDay] = best
            return best
        
        return dp(0, covered)
                




