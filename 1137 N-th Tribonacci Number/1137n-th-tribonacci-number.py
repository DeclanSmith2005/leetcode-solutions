class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        one , two , three = 0, 1, 1
        for i in range(3, n+1):
            curr = one + two + three
            one, two, three = two, three, curr
        return three