class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x: abs(x))
        return [num * num for num in nums]