class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        answer = list(s)
        for i, char in enumerate(s):
            if char == "*":
                if stack:
                    j = stack.pop()
                    answer[j] = ""
                    answer[i] = ""
            else:
                stack.append(i)
            
        return "".join(answer)