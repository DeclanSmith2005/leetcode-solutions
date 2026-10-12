class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}
        res = []
        for i, v in enumerate(numbers):
            if target - v in seen:
                return (seen[target-v]+1, i+1)
            seen[v] = i
        return -1