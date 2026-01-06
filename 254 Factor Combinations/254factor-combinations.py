class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        def rc(num, i, curr):
            while i * i <= num:
                if num % i == 0:
                    other = num // i
                    res.append(curr[:] +[i, other])
                    rc(other, i, curr + [i])
                i+=1
        rc(n,2,[])
        return res
                
            