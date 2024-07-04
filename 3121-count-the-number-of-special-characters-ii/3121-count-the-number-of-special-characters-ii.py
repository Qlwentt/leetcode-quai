class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special = set()
        lowercase = set()
        upper = set()
        for char in word:
            if char.islower():
                lowercase.add(char)
                if char.upper() in special:
                    special.remove(char.upper())
            else:
                if char.lower() in lowercase and char not in upper:
                    special.add(char)
                upper.add(char)
        return len(special)