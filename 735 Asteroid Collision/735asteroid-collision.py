class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            if not stack:
                stack.append(a)
                continue
            if stack[-1] < 0:
                stack.append(a)
                continue
            if a > 0:
                stack.append(a)
                continue
            while stack and stack[-1] < abs(a) and stack[-1] > 0:
                stack.pop()
            if stack and stack[-1] > abs(a):
                continue
            if stack and stack[-1] == abs(a):
                stack.pop()
                continue
            stack.append(a)
        return stack
