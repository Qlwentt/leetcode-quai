class Solution:
    def compressedString(self, word: str) -> str:
        count = 0
        prev = None
        answer = []
        for char in word:
            if prev:
                if char == prev and count < 9:
                    count += 1
                else:
                    answer.append(str(count)+prev)
                    count = 1
            else:
                count += 1
            prev = char
        answer.append(str(count)+prev)
        return "".join(answer)
        