class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for direction, amt in shift:
            amt %= len(s)
            if direction == 0:
                s = s[amt:] + s[:amt]
            else:
                s= s[-amt:] + s[:-amt]
        return s
