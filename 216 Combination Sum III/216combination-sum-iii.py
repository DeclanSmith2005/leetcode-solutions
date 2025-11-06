class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answers = set()
        def backTrack (curr, ind):
            if len(curr) == k and sum(curr) == n:
                answers.add(tuple(curr[:]))
                return
            for i in range (ind, 10):
                curr.append(i)
                backTrack(curr, i+1)
                curr.pop()
        backTrack([], 1)
        return list(answers)
            

        