from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        
        A, B = nums1, nums2
        if len(nums2) < len(nums1):
            A,B = B,A
            
        l = 0
        r = len(A) - 1

        while True:
            midA = l + (r - l) // 2
            midB = half - midA - 2
            
            leftMaxA = A[midA] if midA >= 0 else float('-inf')
            rightMinA = A[midA + 1] if (midA + 1) < len(A) else float('inf')
            leftMaxB = B[midB] if midB >= 0 else float('-inf')
            rightMinB = B[midB + 1] if (midB + 1) < len(B) else float('inf')
            
            # correct partition
            if leftMaxA <= rightMinB and leftMaxB <= rightMinA:
                # even
                if total % 2 == 0:
                    return (max(leftMaxA,leftMaxB) + min(rightMinA, rightMinB)) / 2
                else: #odd
                    return min(rightMinA,rightMinB)
                
            elif rightMinB > leftMaxA:
                l = midA + 1
            else:
                r = midA - 1
    