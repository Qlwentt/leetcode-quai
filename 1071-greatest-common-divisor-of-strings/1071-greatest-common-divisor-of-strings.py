class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def get_divisors(s):
            divisors = []
            for i in range(len(s)):
                times = len(s) // (i+1)
                if s[:i+1] * times == s:
                    divisors.append(s[:i+1])

                        
            return divisors
        
        answer1 = get_divisors(str1)
        answer2 = set(get_divisors(str2))
        
        for answer in answer1[::-1]:
            if answer in answer2:
                return answer
        
        return ""
        
        
        