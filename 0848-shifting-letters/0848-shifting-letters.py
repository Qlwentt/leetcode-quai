class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        postfix_sums = [0] * len(shifts)
        cur_sum = 0
        for i in range(len(shifts)-1,-1,-1):
            cur_sum += shifts[i]
            postfix_sums[i] = cur_sum
        answer = []
        char_to_index = {char: i for i, char in enumerate('abcdefghijklmnopqrstuvwxyz')}
        index_to_char = "abcdefghijklmnopqrstuvwxyz"
        for i, char in enumerate(s):
            shifted_i = (char_to_index[char] + postfix_sums[i]) % 26
            answer.append(index_to_char[shifted_i])
            
        return "".join(answer)
# Time: O(N)
# Space: O(N)

# constant space solution
        postfix_sum = sum(shifts)
        answer = []
        char_to_index = {char: i for i, char in enumerate('abcdefghijklmnopqrstuvwxyz')}
        index_to_char = "abcdefghijklmnopqrstuvwxyz"
        for i, char in enumerate(s):
            shifted_i = (char_to_index[char] + postfix_sum) % 26
            answer.append(index_to_char[shifted_i])
            postfix_sum -= shifts[i]
        return "".join(answer)
# Time: O(N)
# Space: O(1)
        
        