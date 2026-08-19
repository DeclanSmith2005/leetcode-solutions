class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        for h in sorted(counts.keys()):
            size= counts[h]
            if size == 0:
                continue
            for k in range(h, h+ groupSize):
                counts[k] -= size
                if counts[k] < 0:
                    return False
        return True
                
                

        

            
