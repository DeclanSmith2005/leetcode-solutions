class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        retList = []
        def backTrack(base, path):
            if len(path)==k:
                retList.append(path[:])
                return
            
            for i in range(base, n+1):
                path.append(i)
                backTrack(i+1, path)
                path.pop()
            

        backTrack(1,[])
        return retList