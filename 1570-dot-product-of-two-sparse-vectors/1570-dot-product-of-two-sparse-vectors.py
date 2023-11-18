from collections import defaultdict
class SparseVector:
    
    def __init__(self, nums: List[int]):
        self.vector = {}
        for i, num in enumerate(nums):
            self.vector[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        answer = 0
        for i in self.vector.keys():
            if i in vec.vector:
                answer+= self.vector[i] * vec.vector[i]
        return answer

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)