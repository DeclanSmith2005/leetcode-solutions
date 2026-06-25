class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(a, b):
            tmp = s[a]
            s[a] = s[b]
            s[b] = tmp
        l, r = 0, len(s)-1
        while l < r:
            swap(l, r)
            l, r = l + 1, r -1
        