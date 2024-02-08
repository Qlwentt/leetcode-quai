class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {"a": 0, "b": 0, "c": 0}
        # 012345
        #"aaacb" 4+3+2+1
        # L 
        #     R
        
        L = 0
        answer = 0
        for R in range(len(s)):
            count[s[R]] += 1
            while all(value >= 1 for value in count.values()):
                answer += len(s) - R
                count[s[L]] -= 1
                L += 1
        return answer