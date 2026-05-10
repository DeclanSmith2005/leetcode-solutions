class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        volX = 0 # current states for x and y 
        volY = 0
        visited = set()
        if x + y < target:
            return False
        
        def dp (volX, volY):    
            sx, sy = volX, volY
            if volX + volY == target:
                return True
            
            if (volX, volY) in visited:
                return False
            
            visited.add((volX, volY))
            
            volX, volY = x, volY # fill X, y stays same
            a= dp(volX, volY)
            
            volX, volY = sx, y # fill y, x stays same
            b = dp(volX, volY)
            volX, volY = 0, sy # x = 0, y stays same
            c = dp(volX, volY)
            volX, volY = sx, 0 # x same, y = 0 
            d = dp(volX, volY)
            
            tempX, tempY = sx, sy # pour from y to x
            volX = min((tempX + tempY), x)
            volY = max(0, min(tempY, tempY - (x - tempX)))
            e = dp(volX, volY) 

            tempX, tempY = sx, sy # pour from y to x
            volY = min((tempX + tempY), y)
            volX = max(0, min(tempX, tempX - (y - tempY)))
            f = dp(volX, volY) 
                        
            return a or b or c or d or e or f
            
        return dp(0,0)
