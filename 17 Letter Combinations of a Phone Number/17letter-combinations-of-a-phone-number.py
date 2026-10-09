class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(curr, i):
            if len(curr) == len(digits):
                res.append("".join(curr[:]))
                return
            for c in letters[digits[i]]:
                dfs(curr + [c], i+1)

        dfs([], 0)
        return res

