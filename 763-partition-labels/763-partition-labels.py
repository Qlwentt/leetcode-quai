class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastFound = {}
        for i, char in enumerate(s):
            lastFound[char] = i
        
        end = 0
        size = 0
        partitions = []
        
        for i, char in enumerate(s):
            charLastFound = lastFound[char]
            size += 1
            if charLastFound > end:
                end = charLastFound
            if i == end:
                partitions.append(size)
                size = 0
        if size:
            partitions.append(size)
        return partitions