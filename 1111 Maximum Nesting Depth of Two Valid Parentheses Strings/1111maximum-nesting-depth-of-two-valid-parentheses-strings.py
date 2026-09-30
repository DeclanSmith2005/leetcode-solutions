class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        a = 0
        b = 0
        res = []
        for l in seq:
            if l == '(':
                if b < a:
                    b+=1
                    res.append(1)
                else:
                    a+=1
                    res.append(0)
            if l == ')':
                if b >= a:
                    b -= 1
                    res.append(1)
                else:
                    a -=1
                    res.append(0)
        return res

        return res
