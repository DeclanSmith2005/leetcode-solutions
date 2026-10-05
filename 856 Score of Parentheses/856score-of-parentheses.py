class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # keep a stack of the open parenthesis. Every time we close one, we add 2** length of the stack to the score
        stack = []
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append((i, c))
            else:
                op, _ = stack.pop()
                if op == i -1:
                    res += 2**len(stack)
        return res
