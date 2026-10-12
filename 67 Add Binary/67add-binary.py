class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            tmp = a
            a = b
            b = tmp
        a = a[::-1]
        b = b[::-1]
        res = []
        c = 0
        for i in range(len(b)):
            ac, bc = int(a[i]), int(b[i])
            s = ac ^ bc ^ c
            c = ac&bc | ac&c | bc&c
            res.append(str(s))
        
        for i in range(len(b), len(a)):
            ac = int(a[i])
            res.append(str(c ^ ac))
            c = c & ac
        
        if c:
            res.append(str(c))
        
        return "".join(res[::-1])
        
