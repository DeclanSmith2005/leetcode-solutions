class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def check(i):
            return True if i < 0 or i >= len(flowerbed) or flowerbed[i] == 0 else False
        for i in range( len(flowerbed)):
            if check(i-1) and check(i) and check(i+1):
                flowerbed[i] = 1
                n-=1
        return True if n<= 0 else False
            