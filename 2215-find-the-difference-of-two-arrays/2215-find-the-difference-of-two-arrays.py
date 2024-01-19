class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        answer1 = []
        for num in nums1:
            if num not in nums2:
                answer1.append(num)
                
        answer2 = []
        for num in nums2:
            if num not in nums1:
                answer2.append(num)
                
        return [answer1, answer2]