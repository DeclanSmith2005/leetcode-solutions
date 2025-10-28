class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        if n == 0: return 0

        def ways1(ch):
            if ch == '*': return 9
            if ch == '0': return 0
            return 1

        def ways2(a, b):
            if a == '*' and b == '*': return 15
            if a == '*':
                return 2 if '0' <= b <= '6' else 1
            if b == '*':
                if a == '1': return 9   # 11-19 (no 10)
                if a == '2': return 6   # 21-26 (no 20)
                return 0
            val = (ord(a)-48)*10 + (ord(b)-48)
            return 1 if 10 <= val <= 26 else 0

        dp0 = 1
        dp1 = ways1(s[0]) % MOD
        for i in range(1, n):
            cur = (dp1 * ways1(s[i]) + dp0 * ways2(s[i-1], s[i])) % MOD
            dp0, dp1 = dp1, cur
        return dp1
