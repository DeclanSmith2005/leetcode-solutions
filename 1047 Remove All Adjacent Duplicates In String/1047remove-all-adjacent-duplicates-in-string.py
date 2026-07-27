class Solution:
    def removeDuplicates(self, s: str) -> str:
        chars = list(s)
        stack = []
        for c in chars:
            if not stack or stack[-1] != c:
                stack.append(c)
            elif stack:
                stack.pop()
        return "".join(stack)
            