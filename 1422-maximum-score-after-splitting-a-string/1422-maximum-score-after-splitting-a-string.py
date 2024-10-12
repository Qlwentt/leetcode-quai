class Solution:
    def maxScore(self, s: str) -> int:
        prefix_ones = [0] * len(s)
        cur_ones = 0
        for i in range(len(s)-1,-1,-1):
            cur_ones += 1 if s[i] == "1" else 0
            prefix_ones[i] = cur_ones
        
        cur_zeros = 0
        prefix_zeros = []
        for char in s:
            cur_zeros += 1 if char == "0" else 0
            prefix_zeros.append(cur_zeros)
        

        prefix_ones.pop(0)  
        prefix_zeros.pop()
        
        max_score = 0
        for a,b in zip(prefix_ones,prefix_zeros):
            max_score = max(a+b, max_score)
        
        return max_score