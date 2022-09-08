class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = "aeiou"
        vowels = set(vowels)
        newS = []
        for char in s:
            if char not in vowels:
                newS.append(char)
        return "".join(newS)