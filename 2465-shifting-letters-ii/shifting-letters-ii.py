class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        "abc"
       # [-1,-1,2] [0,1,0],[1,2,1],[0,2,1]

        num_letters = [ord(char)-ord('a') for char in s]

        prefix_array = [0]*len(s)

        for l,r, direction in shifts:
            normalized_direction = -1 if direction == 0 else 1
            prefix_array[r] += normalized_direction
            if l > 0:
                prefix_array[l-1] -= normalized_direction
        
        run_sum = 0
        for i in range(len(prefix_array)-1,-1,-1):
            run_sum += prefix_array[i]
            num_letters[i] = (num_letters[i] + run_sum) % 26
        
        return "".join([chr(num + ord('a'))for num in num_letters])

       