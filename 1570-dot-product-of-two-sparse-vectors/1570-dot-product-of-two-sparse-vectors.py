class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = []
        for i, num in enumerate(nums):
            if num != 0:
                self.vector.append((i, num))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        p1 = 0
        p2 = 0
        dotProd = 0
        while p1 < len(self.vector) and p2 < len(vec.vector):
            i1, num1 = self.vector[p1]
            i2, num2 = vec.vector[p2]
           
            if i1 < i2:
                p1 += 1
            elif i2 < i1:
                p2 += 1
            else: # indices match
                dotProd += num1 * num2
                p1 += 1
                p2 += 1
        return dotProd

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)