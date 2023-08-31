class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # [0,0,0,0,1,0,0,0,0] 2 2
        # [1,0,0,0,1]  length 3, capacity 2 or 1
        # 0[1,0,1,0,1,0]1 length 6, capaicty 3 or 2
        # [0,0,0,0,0] length 5 , capacity 3 or 2
        # [0,0,0,0] length 4, capacity 2 or 1
        #  0 1 2 3 4
        # [1,0,0,0,1]
      #      L
      #            R
        #[1,0,0,0,1] 3//2
 #       [0,0,1,0,1]
 #       L
#            R

   #     [1,0,0,0,0,1]
    #      L
    #              R
       #[1,0,0,0,1,0,0]
        L = 0
        R = 0
        capacity = 0
        allZeros = True
        while R < len(flowerbed)+1:
            prev = flowerbed[L-1] if L > 0 else 0
            next_ = flowerbed[R] if R < len(flowerbed) else 0
            if next_ == 1:
                allZeros = False
            if next_ == 1 or R == len(flowerbed):
                capacity+= ((R - L) // 2)
                capacity -= prev and next_ and (R-L) % 2 == 0
                L = R + 1
            R += 1
        
        if allZeros:
            capacity = (len(flowerbed) // 2 ) + len(flowerbed) % 2
                
        return capacity >= n