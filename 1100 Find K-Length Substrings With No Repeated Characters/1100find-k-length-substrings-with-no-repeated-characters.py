class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        l = 0 
        curr = set()
        res = 0
        for r in range(len(s)):
            while s[r] in curr or r-l+1 > k:
                curr.remove(s[l])
                l+=1 
            curr.add(s[r])
            res += 1 if r-l + 1 == k else 0
        return res