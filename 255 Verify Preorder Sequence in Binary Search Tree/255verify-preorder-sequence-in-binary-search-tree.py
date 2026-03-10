class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lowerBound = float('-inf')
        for val in preorder:
            while stack and stack[-1] < val:
                lowerBound = stack.pop()
            if val <= lowerBound:
                return False
            stack.append(val)
        return True
            