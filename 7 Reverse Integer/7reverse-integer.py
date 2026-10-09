class Solution:
    def reverse(self, x: int) -> int:
        mul =1
        if x < 0:
            mul = -1
            x*=-1
        res = int("".join([i for i in str(x)][::-1])) * mul
        return res if -2**31 <= res <= 2**31 -1 else 0 