class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#     [1,4,3,5,6] [4 ,5 ,6 ]
#                 [5, 6,-1]
#  top|
#     |
#     |
#     |
# bot |6
# monotonically increasing
        stack = []
        numToIndex = {num: i for i,num in enumerate(nums1)}
        answer = [-1] * len(nums1)
        for num in nums2:
            while stack and num > stack[-1]:
                top = stack.pop()
                if top in numToIndex:
                    answer[numToIndex[top]] = num
            stack.append(num)
        return answer

        
    