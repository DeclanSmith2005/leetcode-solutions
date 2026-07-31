class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counts = defaultdict(int)
        for v in changed:
            counts[v] += 1
        res = []
        changed.sort()
        for v in changed:
            if v == 0  and counts[v] > 0 and counts[v] %2 == 0:
                counts[v] -= 2
                res.append(v)
            if v!= 0 and counts[2*v] > 0 and counts[v] > 0:
                counts[2*v] -= 1
                counts[v] -=1
                res.append(v)
        return res if len(changed) %2 == 0 and len(changed) == 2* len(res) else []