class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        disallowed = {(1,3):2, (1,9):5, (1,7):4, (2,8):5, (3,7):5, (3,9):6, (4,6):5, (7,9):8}
        res, curr, used = 0, [], set()
        def bt():
            nonlocal res
            if m <= len(curr) <= n:
                res += 1
                if len(curr) == n:
                    return
            for i in range(1,10):
                if i in used:
                    continue
                if curr:
                    a = curr[-1]
                    if (a, i) in disallowed and disallowed[(a, i)] not in used or (i, a) in disallowed and disallowed[(i, a)] not in used:
                        continue
                curr.append(i)
                used.add(i)
                bt()
                curr.pop()
                used.remove(i)
        bt()
        return res
                    

