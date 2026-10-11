class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        n*= 2
        def rc(op, clos, curr):
            if op + clos == n:
                res.append(curr[:])
                return
            if op < n // 2:
                rc(op+1, clos, curr + ['('])
            if clos < op:
                rc(op, clos + 1, curr + [')'])
        rc(0, 0, [])
        return ["".join(l) for l in res]


            