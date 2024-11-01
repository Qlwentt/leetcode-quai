class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = [] # letter, count
        answer = list(s)
        for i, char in enumerate(s):
            if stack and stack[-1][0] == char and stack[-1][1] == 2:
                answer[i] = ""
            else:
                if stack and stack[-1][0] == char:
                    stack[-1][1] += 1
                else:
                    stack.append([char, 1])
        return "".join(answer)