class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openPs = 0
        closePs = 0
        for paren in s:
            if paren == "(":
                openPs += 1
            else:
                if openPs:
                    openPs -= 1
                else:
                    closePs += 1
        return openPs + closePs