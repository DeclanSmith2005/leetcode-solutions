class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = defaultdict(int)
        for l in s:
            counts[l] += 1
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1