class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            arr.sort()
            diff = arr[1] - arr[0]
            
            for i in range(2, len(arr)):
                if arr[i] - arr[i-1] != diff:
                    return False
                
            return True
                    
        answers = []
        for L, R in zip(l,r):
            answers.append(check(nums[L:R+1]))
        return answers            