class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        memo = {}

        def dfs(course):
            if course in memo:
                return memo[course]
            res = set()
            for pre in graph[course]:
                res.add(pre)
                res |= dfs(pre)
            memo[course] = res
            return res

        return [a in dfs(b) for a, b in queries]
        