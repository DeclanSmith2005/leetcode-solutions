class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        j  = float('inf')
        for num in nums:
            while stack and num >= stack[-1][1]: # maintains mono atomic decreasing
                stack.pop()
            if stack and num > stack[-1][0]:
                return True
            j = min (j, num)
            if j < num:
                stack.append([j, num])
        return False
        
