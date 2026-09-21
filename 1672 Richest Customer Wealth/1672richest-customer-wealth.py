class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(acc) for acc in accounts)