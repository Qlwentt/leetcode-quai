class Solution:
    def smallestString(self, s: str) -> str:
        L = 0
        seen_non_a = False  
        broke_early = False                
        for R in range(len(s)):
            if s[R] == "a" and seen_non_a:
                broke_early = True
                break
            elif s[R] == "a" and not seen_non_a:
                L = R+1
            else:
                seen_non_a = True
                
        if L == len(s):
            L -= 1
        if R == len(s) - 1 and not broke_early:
            R += 1
        
        answer = list(s)
        convert = {char: chr(ord(char)-1) for char in "abcdefghijklmnopqrstuvwxyz" }
        convert["a"] = "z"
        
        for i in range(L, R):
            answer[i] = convert[answer[i]]
        return "".join(answer)