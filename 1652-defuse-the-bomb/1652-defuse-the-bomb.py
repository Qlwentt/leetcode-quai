class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
       
        circ_code = code + code
        
        def get_sums(nums,k):
            answer = []
            L = 0
            cur_sum = 0
            for R in range(len(nums)):
                if R-L+1 > k:
                    cur_sum -= nums[L]
                    L += 1
                cur_sum += nums[R]
                if R-L+1 == k:
                    answer.append(cur_sum)
            return answer
        forward_sums = get_sums(circ_code, k)
        backward_sums = get_sums(circ_code[::-1], -k)
        
        for i in range(len(code)):
            code[i] = forward_sums[i+1] if k > 0 else backward_sums[i+1]
        return code if k > 0 else code[::-1]