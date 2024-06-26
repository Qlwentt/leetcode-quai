class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_pal(L,R):
            count = 0
            while L >= 0 and R < len(s):
                if s[L] != s[R]:
                    break
                count += 1
                L -= 1
                R += 1
            return count
        answer = 0
        for i in range(len(s)):
            answer += count_pal(i,i)
            answer += count_pal(i,i+1)
        return answer