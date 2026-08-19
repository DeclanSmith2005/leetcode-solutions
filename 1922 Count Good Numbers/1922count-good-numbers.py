class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(base, exp):
            if exp == 0:
                return 1
            elif exp == 1:
                return base % ((10 ** 9) + 7)
            elif exp % 2 == 0:
                return (power(base, exp // 2) ** 2) % ((10 ** 9) + 7)
            else:
                return (power(base, exp // 2) ** 2) * base % ((10 ** 9) + 7)
        return (power(5, n//2 + n%2) * power(4, n//2)) % ((10 ** 9) + 7)
