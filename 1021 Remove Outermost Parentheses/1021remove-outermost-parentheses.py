class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        q = deque([])
        op, clos = 0, 0
        for c in s:
            if c == '(':
                op +=1
            else:
                clos += 1
            q.append(c)
            if op == clos and len(q) > 1:
                q.popleft()
                q.pop()
                res.extend(list(q))
                q = deque([])
        return "".join(res)
            
            