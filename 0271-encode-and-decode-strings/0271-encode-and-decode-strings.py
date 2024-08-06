class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = []
        for s in strs:
            encoded.append(str(len(s))+"#"+ s)
        return "".join(encoded)
        
    "50#Hello5#World"
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        words = []
        while i < len(s):
            num = 0
            while s[i] != "#":
                num = num * 10 + int(s[i]) 
                i += 1
            words.append(s[i+1:i+1+num])
            i += num + 1
            
        return words
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))