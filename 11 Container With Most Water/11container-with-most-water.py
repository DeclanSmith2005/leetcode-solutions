class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2 ptrs left and right closing from either side of array
        # move the smaller one and compare size of current container with max found
        # return largest container
        l, r = 0 , len(height)-1
        res = 0
        while l <= r:
            res = max(res, (r- l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -=1 
        return res