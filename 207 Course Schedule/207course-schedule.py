class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        children = defaultdict(list)
        state = [0] * numCourses
        for a, b in prerequisites:
            children[b].append(a)
        
        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1
            if all(dfs(n) for n in children[node]):
                state[node] = 2
                return True
            else:
                return False
        
        return all(dfs(n) for n in range(numCourses))
