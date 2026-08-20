class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = Counter(s1)
        for l in string.ascii_lowercase:
            letters[l] = 0 if l not in letters else letters[l]
        counts = defaultdict(int)
        l = 0 
        for r in range(len(s2)):
            counts[s2[r]] += 1
            while counts[s2[r]] > letters[s2[r]]:
                counts[s2[l]] -=1
                l+= 1
            if r-l+1 == len(s1):
                return True
        return False