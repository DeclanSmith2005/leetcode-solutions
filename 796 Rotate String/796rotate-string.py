class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        double = s + s
        for start in range(len(s)):
            if double[start:start+len(s)] == goal:
                return True
        return False