class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = defaultdict(int)
        for i in s:
            counts[i] += 1
        numOdds = 0
        for i in counts.values():
            if i % 2 != 0:
                numOdds+=1
        return numOdds <= 1