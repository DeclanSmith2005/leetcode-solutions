class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # store number of preRequisiites for each course in a hashmap
        # store hashmap course -> courses you can take after that course
        # do topological sort with a q, processing courses that have all prereqs done
        # add these to result list and return
        res = []
        seen = set()
        degree = defaultdict(int)
        children = defaultdict(list)
        for a, b in prerequisites:
            children[b].append(a)
            degree[a] += 1

        s = []
        for course in range(numCourses):
            degree[course] += 0
            if degree[course] == 0:
                s.append(course)
        
        while s:
            curr = s.pop()
            res.append(curr)
            seen.add(curr)
            for child in children[curr]:
                degree[child] -= 1
                if degree[child] == 0 and child not in seen:
                    s.append(child)
        return res if len(res) == numCourses else []



