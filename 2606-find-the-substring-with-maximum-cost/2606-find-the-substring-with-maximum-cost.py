class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        answer = 0
        costs = {char:i+1 for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
        for i, char in enumerate(chars):
            costs[char] = vals[i]
        
        cur_sum = 0
        for R in range(len(s)):
            cur_sum += costs[s[R]]
            if cur_sum < 0:
                cur_sum = 0
            answer = max(cur_sum, answer) 
        
        return answer