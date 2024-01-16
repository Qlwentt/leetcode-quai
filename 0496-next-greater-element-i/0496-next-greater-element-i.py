class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#     [1,4,3,5,6] [4 ,5 ,6 ]
#     [6,5,4]
#     [4,3,5,6,0]
     # monotonically decreasing - go in reverse
        indices = {num:i for i,num in enumerate(nums1)}
        answer = [-1] * len(nums1)
        stack = []
        #[1,3,4,2]
        for i in range(len(nums2)-1,-1,-1):
            num = nums2[i]
            while stack and num >= stack[-1]:
                stack.pop()
            if stack and num in indices:
                answer[indices[num]] = stack[-1]
            stack.append(num)
        
        return answer



        
    