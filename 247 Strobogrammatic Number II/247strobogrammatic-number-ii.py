class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1:
            return ["0","1","8"]
        pairs = [(0,0), (1,1), (6,9), (8,8), (9,6)]
        res = []
        curr = []

        def  bt():
            nonlocal res, curr
            if len(curr) >= n:
                return
            for a, b in pairs:
                curr = [a] + curr + [b]
                if len(curr) == n:
                    res.append(curr)
                bt()
                curr = curr[1:-1] 
        
        if n%2 == 0:
            bt()
        else:
            for i in ([0,1,8]):
                curr = [i]
                bt()
        return (["".join(map(str, x)) for x in res if len(str(int("".join(map(str, x))))) == len("".join(map(str, x)))])
