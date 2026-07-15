class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        eSum, oSum = 0 , 0 
        for i in range(2*n):
            if i % 2 == 0:
                eSum += i
            else:
                oSum += i 

        # problem passed but next step would be binary search over the range of possible GCDs
        # nvm math answer has aura
        for i in range(min(oSum, eSum), 0, -1):
            if oSum % i == 0 and eSum % i == 0:
                return i
        return 1