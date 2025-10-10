class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        parents = list(range(n))
        logs.sort()
        total = n
        for t, x, y in logs:
            # print(parents)
            while parents[x] != x or parents[y] != y:
                x = parents[x]
                y = parents[y]
            if x != y:
                parents[x] = y
                total -= 1
                if total == 1:
                    return t
        return -1