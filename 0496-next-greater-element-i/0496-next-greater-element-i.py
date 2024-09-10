class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_i = {num: i for i, num in enumerate(nums1)}
        
        stack = [] # 
        answer = [-1] * len(nums1)
        for num in nums2:
            while stack and stack[-1] < num:
                lesser = stack.pop()
                if lesser in num_to_i:
                    answer[num_to_i[lesser]] = num
            stack.append(num)
        return answer
    
# Time: O(N)
# Space: O(N)
                