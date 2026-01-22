class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        inDegree = defaultdict(int)
        completed = 0
        for i in range(1, n+1):
            inDegree[i] += 0
        nbrs = defaultdict(list)
        for prev, nxt in relations:
            inDegree[nxt] += 1
            nbrs[prev].append(nxt)
        courses = deque([])
        for i in range(1, n+1):
            if inDegree[i] == 0:
                courses.append(i)
        res = 0
        while courses:
            res += 1
            for i in range(len(courses)):
                curr = courses.pop()
                for c in nbrs[curr]:
                    inDegree[c] -= 1
                    if inDegree[c] == 0:
                        courses.appendleft(c)
                completed += 1
        return -1 if completed != n else res

        