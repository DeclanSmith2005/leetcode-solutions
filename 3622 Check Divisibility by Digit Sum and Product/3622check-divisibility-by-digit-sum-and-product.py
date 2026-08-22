class Solution:
    def checkDivisibility(self, n: int) -> bool:
        mul = 1
        for i in str(n):
            mul *= int(i)
        return not n % (sum(int(i) for i in str(n)) + mul)