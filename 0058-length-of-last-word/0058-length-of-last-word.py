class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        s = [oneS for oneS in s if oneS != ""]
        return len(s[-1])