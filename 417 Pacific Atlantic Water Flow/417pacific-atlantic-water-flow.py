class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # starting from bottom left and top right corners, validate spreading out coords
        # that are immediately higher than a preceding square and mark all such squares
        # as being valid for the output
        ret = []
        dp = [[0 for col in range(len(heights[0]))] for row in range(len(heights))]
        
       
        def  check (row, col ):
            pacific = False
            atlantic = False
            visited = set()

            def recurse(r, c):
                nonlocal pacific
                nonlocal atlantic
                nonlocal visited
                
                if r < 0 or r > len(heights)-1 or c < 0 or c > len(heights[0])-1 or (r,c) in visited:
                    return False
                visited.add((r,c))
                if r == 0 or c == 0:
                    pacific = True
                if r == len(heights)-1 or c == len(heights[0])-1:
                    atlantic = True
                if (pacific and atlantic) or dp[r][c]:
                    return True 
                curr = heights[r][c]
                if r < len(heights)-1 and heights[r+1][c] <= curr and recurse(r+1, c):
                    return True
                elif r > 0 and heights[r-1][c] <= curr and recurse(r-1, c):
                    return True
                elif c < len(heights[0])-1 and heights[r][c+1] <= curr and recurse(r, c+1):
                    return True
                elif c > 0 and heights[r][c-1] <= curr and recurse(r, c-1):
                    return True
                else:
                    return False
                

            if recurse(row, col):
                dp[row][col]= 1
                ret.append([row, col])

        for level in range(len(heights)):
            for column in range(len(heights[0])):
                check(level, column)
        return ret
            