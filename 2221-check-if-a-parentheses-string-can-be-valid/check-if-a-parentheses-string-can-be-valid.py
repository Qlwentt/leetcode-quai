class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        length = len(s)

        # If length of string is odd, return false.
        if length % 2 == 1:
            return False

        open_brackets = []
        unlocked = []

        # Iterate through the string to handle '(' and ')'
        for i in range(length):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                open_brackets.append(i)
            elif s[i] == ")":
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        # Match remaining open brackets and the unlocked characters
        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()

        if open_brackets:
            return False

        return True
