class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 1
        currentRange = []
        outList = []
        n = len(nums)
        if n == 0:
            return currentRange
        currentRange.append(nums[0])
        CRLen = 0 
        for i in range(1, len(nums)):
            if  nums[i] == nums[i-1]+1:
                currentRange.append(nums[i])
                CRLen += 1
            else: 
                if CRLen == 0:
                    outList.append(str(currentRange[0]))
                else:     
                    outList.append(f"{currentRange[0]}->{currentRange[CRLen]}")
                CRLen = 0
                currentRange = [nums[i]]
        if CRLen == 0:
            outList.append(str(currentRange[0]))
        else:     
            outList.append(f"{currentRange[0]}->{currentRange[CRLen]}")
            CRLen = 0
            currentRange = [nums[i]]
        return outList
