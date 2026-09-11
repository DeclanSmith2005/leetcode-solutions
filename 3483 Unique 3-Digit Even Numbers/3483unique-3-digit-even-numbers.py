class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        counts = Counter(digits)
        seen = set()
        res= 0
        for first in digits:
            if first == 0:
                continue
            counts[first] -= 1
            for second in digits:
                if counts[second] == 0:
                    continue
                counts[second]-=1
                for third in digits:
                    if third %2 != 0 or counts[third] == 0 or (first, second, third) in seen:
                        continue
                    seen.add((first, second, third))
                    res +=1
                counts[second] += 1
            counts[first] += 1
                
        return res
                    