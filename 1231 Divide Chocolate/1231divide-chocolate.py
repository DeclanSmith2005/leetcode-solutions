class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def valid(swt):
            peices = 0
            curr = 0 
            for i in range(len(sweetness)):
                curr += sweetness[i]
                if curr >= swt:
                    peices +=1
                    curr = 0
                if peices == k + 1:
                    return True
            return False
            
        l, r = 0, sum(sweetness) // (k + 1)
        while l < r:
            m = (l+r)//2
            if valid(m):
                l  = m + 1
            else:
                r = m 
         
        return l if valid(l) else l - 1
