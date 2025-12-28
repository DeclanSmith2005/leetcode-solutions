class Solution:
    def confusingNumber(self, n: int) -> bool:
        check = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        q = deque([])
        for c in str(n):
            if c not in check:
                return False
            else:
                q.appendleft(check[c])
        return False if int("".join(q)) == n else True
        