class Solution:
    def trap(self, height: List[int]) -> int:
        # min(i-1,i+1) - i
        # 0 0,3 = 0 - 0 = 0 = 0
        # 1 1,3 = 1 - 1 = 0
        # 2 1,3 = 1 - 0 = 1
        # 3 2,3 = 2 - 2 = 0
        # 4 2,3 = 2 - 1 = 1
        # 5 2,3 = 2 - 0 = 2
        # 6 2,3 = 2 - 1 = 1
        # 7 3,3 = 3 - 3 = 0
        # 8 2,3 = 2 - 2 = 0
        # 9 2,3 = 2 - 1 = 1
        # 0 2,3 = 2 - 2 = 0
        # 1 1,3 = 1 - 1 = 0
        
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        # [3,3,3,3,3,3,3,3,2,2,2,1]
        # [0,1,1,2,2,2,2,3,3,3,3,3]
        #  0 1 2 3 4 5 6 7 8 9 0 1
        
        Lmaxes = [0] * len(height)
        Rmaxes = [0] * len(height)
        
        Lmax = 0
        for i in range(len(height)):
            Lmax = max(Lmax, height[i])
            Lmaxes[i] = Lmax
        
        Rmax = 0
        for i in range(len(height)-1, -1 , -1):
            Rmax = max(Rmax,height[i])
            Rmaxes[i] = Rmax
            
        water = 0
        for i, elevation in enumerate(height):
            water += min(Lmaxes[i], Rmaxes[i]) - elevation
            
        return water
            
        