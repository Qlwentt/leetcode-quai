
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        answer = []
        for s in strs:
            answer.append(str(len(s))+"#"+ s)
        return "".join(answer)
        
        
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        answer = []
        i = 0
        while i < len(s):
            length = []
            while s[i] != "#":
                length.append(s[i])
                i += 1
            length = int("".join(length))
            answer.append(s[i+1:i+1+length])
            i = i + 1 + length
        return answer

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))