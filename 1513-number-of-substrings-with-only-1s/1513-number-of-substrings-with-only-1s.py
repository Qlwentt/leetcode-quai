class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        answer = 0 
            
        for item in s:
            if item == "1":
                count += 1
                answer += count
            else:
                count = 0
        return answer % (10**9 + 7)