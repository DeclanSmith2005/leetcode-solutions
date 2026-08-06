class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, 101):
            product = 1
            for k in str(i):
                product *= int(k)
            if product % t == 0:
                return i
        