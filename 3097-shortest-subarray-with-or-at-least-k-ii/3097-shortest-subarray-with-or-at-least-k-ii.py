class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        bits_map = [0] * 32
        answer = float('inf') 
                             
        for r in range(len(nums)):
            for i in range(32):
                bits_map[i] += 1 if nums[r] & (1 << i) else 0
            
            while l <= r and int("".join(["1" if num > 0 else "0" for num in bits_map][::-1]),2) >= k:
                answer = min(answer, r-l+1)
                for i in range(32):
                    bits_map[i] -= 1 if nums[l] & (1 << i) else 0
                l += 1
            
        return answer if answer != float('inf') else -1
                