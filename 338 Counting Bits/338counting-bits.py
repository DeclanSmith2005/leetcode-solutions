class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        for i in range(n+1):
            string = bin(i)[2:]
            for num in string:
                if num == '1':
                    res[i]+= 1
        return res