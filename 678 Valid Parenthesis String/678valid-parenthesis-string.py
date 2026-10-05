class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = []
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == '*':
                stars.append(i)
            else:
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        while stack:
            if not stars or stack.pop() > stars.pop():
                return False
        return True
