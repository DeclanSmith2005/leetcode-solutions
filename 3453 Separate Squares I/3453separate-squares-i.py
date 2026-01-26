class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def check(cut):
            lower, upper = 0, 0
            for x, y, length in squares:
                if y >= cut:
                    upper += length**2
                elif y + length <=  cut:
                    lower += length**2
                else:
                    upper += (y + length - cut )* length
                    lower += (cut - y) * length
            return upper <= lower
        l , r = min(i[1] for i in squares)-1, max(i[1] + i[2] for i in squares)
        while r - l > 10**-5:
            m = (l+r) / 2
            if check(m):
                r= m
            else:
                l =  m
        return l
    

#     Invariant: answer is in [l, r) (left inclusive, right exclusive).
# Think: l is “definitely too low,” r is “a candidate.”
# Initialize: l = 0, r = n (note: r = n, not n-1)
# Loop condition: while l < r
# Mid: m = (l + r) // 2
# Updates (for “first true”):
# if predicate(m) is true → r = m (keep m; it might be the first true)
# else → l = m + 1 (discard m)
# At the end, l == r is the boundary index.
        
