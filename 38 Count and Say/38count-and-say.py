class Solution:
    def countAndSay(self, n: int) -> str:
        def RLE(num):
            curr = str(num)
            res = []
            l = 0
            for r in range(len(curr)+1):
                if r == len(curr) or curr[r] != curr[l]:
                    res.append(f"{r - l}{curr[l]}")
                    l = r
            return "".join(res)

        def CAS(num):
            return "1" if num == 1 else RLE(CAS(num-1))
            
        return CAS(n)

            
