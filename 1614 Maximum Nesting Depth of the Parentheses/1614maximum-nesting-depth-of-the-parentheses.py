class Solution:
    def maxDepth(self, s: str) -> int:
        curr = 0
        res = 0
        for l in s:
            if l == '(':
                curr += 1
            elif l == ')':
                curr -= 1
            res = max(res, curr)
        return res