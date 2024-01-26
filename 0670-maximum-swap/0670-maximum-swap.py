class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        
        last = {num: i for i, num in enumerate(s)}
        
        for i, digit in enumerate(s):
            for laterDigit in range(9, int(digit), -1):
                laterDigit = str(laterDigit)
                if laterDigit in last and last[laterDigit] > i:
                    j = last[laterDigit]
                    s[i], s[j] = s[j], s[i]
                    return int("".join(s))
                
        return num
    
# Time: O(N) because inner loop only goes from at worst case 9 to 0
# Space: O(N) for hashmap and s
        