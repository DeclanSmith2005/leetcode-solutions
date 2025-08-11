class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lowestGap = -1
        for i in range(len(digits)):
            if digits[i] < 9:
                lowestGap = i
        if lowestGap  == -1:
            return [1] + [0]*len(digits)
        else:
            i = len(digits)-1
            while (i>lowestGap):
                digits[i] = 0
                i-=1
            digits[lowestGap]+=1
            return digits
