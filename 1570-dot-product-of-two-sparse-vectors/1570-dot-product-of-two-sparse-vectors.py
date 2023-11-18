from collections import defaultdict
class SparseVector:
    
    def __init__(self, nums: List[int]):
        self.vector = []
        for i, num in enumerate(nums):
            self.vector.append((i,num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        answer = 0
        p1 = 0
        p2 = 0
        
        while p1 < len(self.vector) and p2 < len(vec.vector):
            if self.vector[p1][0] == vec.vector[p2][0]:
                answer += self.vector[p1][1] * vec.vector[p2][1]
                p1 += 1
                p2 += 1
            elif self.vector[p1][0] < vec.vector[p2][0]:
                p1 += 1
            else:
                p2 += 1
        return answer

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)