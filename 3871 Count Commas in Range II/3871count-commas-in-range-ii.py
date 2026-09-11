class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        # first find how many above last comma (multiple of 3 digits) we are
        while n > 999:
            commas = (len(str(n))-1) // 3
            base = 10**(3*(commas))
            res += (n-base+1) * commas
            n = base - 1
            #print(n, base, commas, res)
        return res
