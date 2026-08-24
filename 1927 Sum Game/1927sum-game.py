class Solution:
    def sumGame(self, num: str) -> bool:
        # get sum left, sum right, and number of ? on both sides
        # bob always picks the number that either closes the gap the most or widens it the least
        # alice always widens it the most or closes it the least
        lc, lsum, rc, rsum = 0, 0 , 0 , 0
        for i in range(len(num)//2):
            lc += num[i] == '?'
            lsum += int(num[i]) if num[i] != '?' else 0
        
        for i in range(len(num)//2, len(num)):
            rc += num[i] == '?'
            rsum += int(num[i]) if num[i] != '?' else 0
        
        if lc + rc == 0:
            return lsum != rsum
        
        if (lc + rc) % 2:
            return True
        else:
            if lc == rc:
                return lsum != rsum
            else:
                diff = abs(rc - lc)
                return 9*(rc - lc) !=  2*(lsum - rsum)
                


            
        
