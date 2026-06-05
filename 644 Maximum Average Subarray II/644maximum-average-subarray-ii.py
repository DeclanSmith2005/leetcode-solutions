class Solution:
    def findMaxAverage(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        def d(x, y):
            return (P[y+1] - P[x]) / float(y+1-x)

        hull = collections.deque()
        ans = float('-inf')

        for j in range(K-1, N):
            while len(hull) >= 2 and d(hull[-2], hull[-1]-1) >= d(hull[-2], j-K):
                hull.pop()
            hull.append(j-K + 1)
            while len(hull) >= 2 and d(hull[0], hull[1]-1) <= d(hull[0], j):
                hull.popleft()
            ans = max(ans, d(hull[0], j))

        return ans