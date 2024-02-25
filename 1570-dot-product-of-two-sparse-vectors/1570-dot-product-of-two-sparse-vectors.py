class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = []
        for i, num in enumerate(nums):
            if num != 0:
                self.vector.append((i, num))  

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, v2: 'SparseVector') -> int:
        p1 = 0
        p2 = 0
        answer = 0
        while p1 in range(len(self.vector)) and p2 in range(len(v2.vector)):
            if self.vector[p1][0] < v2.vector[p2][0]:
                p1 += 1
            elif v2.vector[p2][0] < self.vector[p1][0]:
                p2 += 1
            else: # equal
                answer += self.vector[p1][1] * v2.vector[p2][1]
                p1 += 1
                p2 += 1
        return answer
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)