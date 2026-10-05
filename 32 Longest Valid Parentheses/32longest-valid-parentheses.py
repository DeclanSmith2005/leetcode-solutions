class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # looking for the longest sub string of s where the count of "(" == count ")"
        # at no point in the chosen substring can the count dip below the start count 
        left = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            else:
                left.pop()
                if not left:
                    left.append(i)
                else:
                    res= max(res, i - left[-1])
        return res


        
        