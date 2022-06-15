from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        output = []
        for s in strs:
            prefix = str(len(s)) + "#"
            output.append(prefix+s)
        return "".join(output)
# O(n) time
# O(n) space     

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        output = []
        start = 0
        while start < len(s):
            delimiterPosition = start + 1
            while s[delimiterPosition] != '#':
                delimiterPosition += 1
            length = int(s[start:delimiterPosition])
            output.append(s[delimiterPosition + 1:delimiterPosition + 1 + length])
            start = delimiterPosition + 1 + length
        return output
# O(n) time
# O(1) space (not counting output array)
