class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prevflowidx = -math.inf
        i = 0
        while n > 0 and i < len(flowerbed):
            if flowerbed[i] == 0 and prevflowidx != i-1:
                if (i-1 >= 0 and flowerbed[i-1] == 1) or (i+1 < len(flowerbed) and flowerbed[i+1]==1):
                    i += 1
                    continue
                else:
                    n -= 1
                    prevflowidx = i
            i += 1
        return n==0
        
            
                
        