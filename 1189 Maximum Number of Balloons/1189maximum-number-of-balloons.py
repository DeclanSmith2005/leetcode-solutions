class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = defaultdict(int)
        res = 0
        for l in text:
            counts[l] += 1
        while True:
            for l in 'balloon':
                counts[l] -=1
                if counts[l] == -1:
                    return res
            res +=1 
        