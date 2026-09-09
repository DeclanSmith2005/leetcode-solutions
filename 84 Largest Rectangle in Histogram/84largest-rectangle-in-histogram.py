class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = float('-inf')
        heights.append(0) # since the current index isn't icluded in the compressed left rectangle, we can add a final rectantle of height 0 so that any leftover rectangles at the end can be processed 
        stack = [] # (ind, height)
        for i, h in enumerate(heights):
            l, LH = i , h
            while stack and stack[-1][1] >= h:
                l, LH = stack.pop()
                res = max(LH, res, (i - l) * LH)
            stack.append((l, h))
        return res


       
