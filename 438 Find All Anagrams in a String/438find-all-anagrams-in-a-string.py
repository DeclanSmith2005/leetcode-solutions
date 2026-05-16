class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(s) < len(p):
            return []
        counts = [0]* 26
        countsp = [0]* 26
        for i in range(len(p)):
            countsp[ord(p[i]) - ord('a')] += 1
            counts[ord(s[i]) - ord('a')] += 1
        if countsp == counts:
            res.append(0)
        l= 0
        for r in range(len(p),len(s)):
            counts[ord(s[r]) - ord('a')] += 1
            counts[ord(s[l]) - ord('a')] -= 1
            l+=1
            if all(counts[i] == countsp[i] for i in range(len(counts))):
                res.append(l)
        return res