class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif stack:
                stack.pop()
            else:
                res += 1
        while stack:
            stack.pop()
            res += 1
        return res
