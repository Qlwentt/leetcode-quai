class Solution:
    def trap(self, height: List[int]) -> int:
#         # min(L,R) - h[i]
        
#         Lmaxes = [0] * len(height)
#         Rmaxes = [0] * len(height)
        
#         Lmax = 0
#         for i in range(len(height)):
#             Lmax = max(Lmax, height[i])
#             Lmaxes[i] = Lmax
        
#         Rmax = 0
#         for i in range(len(height)-1, -1 , -1):
#             Rmax = max(Rmax,height[i])
#             Rmaxes[i] = Rmax
            
#         water = 0
#         for i, elevation in enumerate(height):
#             water += min(Lmaxes[i], Rmaxes[i]) - elevation
            
#         return water
        L = 0
        R = len(height) - 1
        
        water = 0
        Lmax = 0
        Rmax = 0
        while L < R:
            if height[L] < height[R]:
                Lmax = max(Lmax, height[L])
                water += Lmax - height[L]
                L +=1
            else:
                Rmax = max(Rmax, height[R])
                water += Rmax - height[R]
                R -= 1
        return water
                
            
            
        