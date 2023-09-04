class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
    # [10,1,5,6,2,10]
    # [2,1,5,6,2,3]
    # [3,1,5,10,6,2,2,3,0] 3,10,6,15,
#      L  
#    [1,2,2,3]
   #[1,2,3,4,5,6] 6, 10, 12, 12, 10, 6
   #           L  
 #    num*(len - L) 


 # Brute Force
 # # find highest minimum for longest subarray
        # largestArea = 0
        # for i in range(len(heights)):
        #     for j in range(i,len(heights)):
        #         curMin = min(heights[i:j+1])
        #         largestArea = max(largestArea, curMin * (j-i+1))
        # return largestArea
# [2,1,2] 2,
#[1,2,0]
        heights.append(0)
        stack = [] # value, index
        largestArea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                height, index = stack.pop()
                largestArea = max(largestArea, (i - index) * height)
                start = index
            stack.append((h,start))
        return largestArea
                