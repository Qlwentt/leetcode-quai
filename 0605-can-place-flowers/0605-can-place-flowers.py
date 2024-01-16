class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placed = 0
        for i in range(len(flowerbed)):
            left = flowerbed[i-1] if i-1 in range(len(flowerbed)) else 0
            right = flowerbed[i+1] if i+1 in range(len(flowerbed)) else 0
            if flowerbed[i] == 0 and left == 0 and right == 0:
                placed += 1
                flowerbed[i] = 1
        return placed >= n
            
            