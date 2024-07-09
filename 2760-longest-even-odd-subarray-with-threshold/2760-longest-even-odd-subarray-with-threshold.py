class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        target = 0
        L = 0
        answer = 0
        R = 0
        while R < len(nums):
            if nums[R] % 2 != target or nums[R] > threshold:
                while R < len(nums):
                    if nums[R] % 2 == 0 and nums[R] <= threshold:
                        L = R
                        answer = max(answer, R-L+1)
                        target ^= 1
                        break
                    else:
                        R += 1  
            else:
                answer = max(answer, R-L+1)
                target ^= 1
                R += 1
        return answer
            