class Solution:
    def minOperations(self, s: str) -> int:
        zero_first_count = 0
        one_first_count = 0
        
        zero_first = 0
        one_first = 1
        
        for char in s:
            if int(char) != zero_first:
                zero_first_count += 1
            if int(char) != one_first:
                one_first_count += 1
            zero_first ^= 1
            one_first ^= 1
        
        return min(zero_first_count, one_first_count)
        
        
        