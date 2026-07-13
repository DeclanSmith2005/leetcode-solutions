class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        def rc(curr, ind):
            print(curr)
            if curr and low <= int("".join(curr))  <= high:
                res.append(int("".join(curr)))
            if ind > 9 or (curr and int("".join(curr)) > high):
                return
            curr.append(str(ind))
            rc(curr, ind + 1)
        for i in range(1, 9):
            rc([], i)
        return sorted(res)
        