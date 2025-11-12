class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        sspells = sorted(spells)
        ans = {}
        res = [0]*len(spells)
        i , k =  len(sspells)-1 , 0
        while i > -1:
            if sspells[i] not in ans:
                while k < len(potions) and sspells[i] * potions[k] < success:
                    k+=1
                ans[sspells[i]] = len(potions) - k
            i-=1 
        for i in range(len(spells)):
            res[i] = ans[spells[i]]
        return res
        
            
            