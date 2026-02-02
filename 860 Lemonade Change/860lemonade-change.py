class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counts = defaultdict(int)
        for i in bills:
            counts[i] += 1
            if i == 10:
                if counts[5] > 0:
                    counts[5]-=1
                else:
                    return False
            elif i == 20:
                if counts[10] >= 1 and counts[5]>=1:
                    counts[10], counts[5] = counts[10]-1, counts[5] -1
                else:
                    if counts[5]>=3:
                        counts[5]-=3
                    else:
                        return False
        return True
        