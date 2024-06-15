class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word for word in re.sub(r'\s+', " ", s).split(" ") if word != ""][::-1])
        